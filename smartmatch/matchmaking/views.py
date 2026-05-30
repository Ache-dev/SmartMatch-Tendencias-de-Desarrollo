from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from matchmaking.ml.predictor import predecir_match

# CRUD Base de Personas
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# Endpoint 1: Predicción individual entre dos personas específicas
@api_view(['POST'])
def predict_match(request):
    try:
        persona1_id = request.data['persona1_id']
        persona2_id = request.data['persona2_id']
        
        p1 = Person.objects.get(id=persona1_id)
        p2 = Person.objects.get(id=persona2_id)
    except (KeyError, Person.DoesNotExist):
        return Response({"error": "IDs inválidos o personas no encontradas"}, status=status.HTTP_400_BAD_REQUEST)

    edad_diff = abs(p1.edad - p2.edad)
    mismo_deporte = int(p1.deporte == p2.deporte)
    misma_musica = int(p1.musica == p2.musica)
    misma_mascota = int(p1.mascota == p2.mascota)
    misma_personalidad = int(p1.personalidad == p2.personalidad)

    datos = [edad_diff, mismo_deporte, misma_musica, misma_mascota, misma_personalidad]
    resultado = predecir_match(datos)

    return Response({
        "persona1": p1.nombre,
        "persona2": p2.nombre,
        "datos_modelo": {
            "edad_diff": edad_diff,
            "mismo_deporte": mismo_deporte,
            "misma_musica": misma_musica,
            "misma_mascota": misma_mascota,
            "misma_personalidad": misma_personalidad
        },
        "resultado_ia": resultado
    })

# Endpoint 2: Top de candidatos ideales para un usuario base
@api_view(['GET'])
def top_matches(request, person_id):
    try:
        persona_base = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Persona base no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    personas = Person.objects.exclude(id=person_id)
    resultados = []

    for persona in personas:
        edad_diff = abs(persona_base.edad - persona.edad)
        mismo_deporte = int(persona_base.deporte == persona.deporte)
        misma_musica = int(persona_base.musica == persona.musica)
        misma_mascota = int(persona_base.mascota == persona.mascota)
        misma_personalidad = int(persona_base.personalidad == persona.personalidad)

        datos = [edad_diff, mismo_deporte, misma_musica, misma_mascota, misma_personalidad]
        resultado_ia = predecir_match(datos)

        resultados.append({
            "persona": persona.nombre,
            "probabilidad": resultado_ia["probabilidad"],
            "match": resultado_ia["match"]
        })

    # Ordenar el arreglo por mayor probabilidad descendente
    resultados = sorted(resultados, key=lambda x: x["probabilidad"], reverse=True)
    return Response(resultados)