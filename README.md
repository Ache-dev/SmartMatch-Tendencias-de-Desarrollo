# SmartMatch

Proyecto Django para un sistema de matchmaking con componentes de machine learning.

## Requisitos

- Python 3.8+ (recomendado 3.10 o 3.11)
- Virtualenv o venv
- Git
- (Opcional) Docker

Paquetes Python sugeridos (si no existe `requirements.txt`):

- Django
- djangorestframework
- numpy
- pandas
- scikit-learn
- joblib

## Instalación (local)

1. Clona el repositorio:

```bash
git clone <tu-repo-url>
cd smartmatch
```

2. Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala dependencias:

Si existe `requirements.txt` en la raíz:

```bash
pip install -r requirements.txt
```

Si no existe, instala paquetes mínimos:

```bash
pip install Django djangorestframework numpy pandas scikit-learn joblib
```

4. Aplica migraciones y crea superusuario:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Ahora la aplicación debería estar disponible en `http://127.0.0.1:8000`.

## Estructura relevante del proyecto

- `manage.py` – comando de administración de Django.
- `matchmaking/` – aplicación principal con modelos, vistas y endpoints.
- `matchmaking/ml/` – scripts de machine learning:
  - `dataset_generator.py` — generación de datasets de ejemplo.
  - `train_model.py` — script para entrenar y guardar el modelo.
  - `predictor.py` — script/funciones para cargar el modelo y hacer predicciones.

## Uso del componente ML

1. Generar/obtener datos (si aplica):

```bash
python matchmaking/ml/dataset_generator.py
```

2. Entrenar el modelo:

```bash
python matchmaking/ml/train_model.py
```

El script debería guardar el modelo entrenado (por ejemplo `model.joblib` o similar) en la carpeta que elija el script.

3. Realizar predicciones:

```bash
python matchmaking/ml/predictor.py
```

O importar las funciones desde `matchmaking.ml.predictor` dentro de la aplicación Django para integrarlas en las vistas/serializers.

## Ejecutar tests

```bash
python manage.py test
```

## Notas finales

- Si quieres, puedo generar un `requirements.txt` con las dependencias reales del proyecto.
- Si prefieres, puedo añadir instrucciones para desplegar con Docker o configurar variables de entorno (`.env`).

Si necesitas que lo traduzca, amplíe o añada pasos concretos para producción, dímelo y lo hago.
