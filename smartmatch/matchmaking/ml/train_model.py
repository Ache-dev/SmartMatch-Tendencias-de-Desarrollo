import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from matchmaking.models import MatchTraining

def entrenar_modelo():
    # 1. Obtener los datos desde el modelo ORM de Django
    query = MatchTraining.objects.all().values()
    df = pd.DataFrame(list(query))

    if df.empty:
        print("Error: No hay datos en MatchTraining para entrenar. Genera el dataset primero.")
        return

    # 2. Separar características (X) y variable objetivo (y)
    X = df[['edad_diff', 'mismo_deporte', 'misma_musica', 'misma_mascota', 'misma_personalidad']]
    y = df['match']

    # 3. Instanciar y ajustar (fit) el modelo de Regresión Logística
    model = LogisticRegression()
    model.fit(X, y)

    # 4. Definir la ruta física y guardar el archivo .pkl
    # Lo guardamos en la misma carpeta donde reside este script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'model.pkl')
    
    joblib.dump(model, model_path)
    print(f"Modelo entrenado exitosamente. Guardado en: {model_path}")