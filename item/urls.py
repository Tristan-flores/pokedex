from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonItemViewSet

app_name = "objects"

router = DefaultRouter()
router.register("items", PokemonItemViewSet, basename="item")

urlpatterns = [
    path("", include(router.urls)),
]
