import os
from matchmaking.models import Person, MatchTraining

def generar_dataset():
    # Obtener todas las personas
    personas = list(Person.objects.all())

    # Limpiar dataset anterior
    MatchTraining.objects.all().delete()

    # Comparar todas las personas sin repetir parejas
    for i in range(len(personas)):
        for j in range(i + 1, len(personas)):
            p1 = personas[i]
            p2 = personas[j]

            # Diferencia de edad
            edad_diff = abs(p1.edad - p2.edad)

            # Comparaciones binarias (1 o 0)
            mismo_deporte = int(p1.deporte == p2.deporte)
            misma_musica = int(p1.musica == p2.musica)
            misma_mascota = int(p1.mascota == p2.mascota)
            misma_personalidad = int(p1.personalidad == p2.personalidad)

            # Regla inicial de compatibilidad (heurística)
            puntos = mismo_deporte + misma_musica + misma_mascota + misma_personalidad

            if puntos >= 3 and edad_diff <= 5:
                match = 1
            else:
                match = 0

            # Guardar en la base de datos de entrenamiento
            MatchTraining.objects.create(
                edad_diff=edad_diff,
                mismo_deporte=mismo_deporte,
                misma_musica=misma_musica,
                misma_mascota=misma_mascota,
                misma_personalidad=misma_personalidad,
                match=match
            )

    print("Dataset generado correctamente")