from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from matchmaking.views import PersonViewSet, predict_match, top_matches

# Configuramos el router para el CRUD automático de Personas
router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predict-match/', predict_match),
    path('top-matches/<int:person_id>/', top_matches),
]