import os
import joblib
import numpy as np

def predecir_match(datos):
    # Encontrar la ruta del modelo guardado
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'model.pkl')

    if not os.path.exists(model_path):
        return {"error": "El modelo de IA no ha sido entrenado todavía.", "match": 0, "probabilidad": 0.0}

    # Cargar el modelo entrenado
    model = joblib.load(model_path)

    # Convertir el vector de entrada en una estructura bidimensional que scikit-learn entienda
    # datos = [edad_diff, mismo_deporte, misma_musica, misma_mascota, misma_personalidad]
    input_vector = np.array(datos).reshape(1, -1)

    # Predicción binaria (0 o 1)
    prediccion = int(model.predict(input_vector)[0])

    # Probabilidad del match (Devuelve una lista con [prob_de_0, prob_de_1])
    probabilidades = model.predict_proba(input_vector)[0]
    probabilidad_match = round(float(probabilidades[1]) * 100, 2) # Porcentaje de que sea 1

    return {
        "match": prediccion,
        "probabilidad": probabilidad_match
    }