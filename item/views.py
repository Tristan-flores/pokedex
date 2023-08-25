from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .filters import PokemonItemFilter
from .models import PokemonItem
from .serializers import PokemonItemSerializer


class PokemonItemViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to display all creature items"""

    permission_classes = [
        AllowAny,
    ]
    queryset = PokemonItem.objects.all().order_by("name")
    serializer_class = PokemonItemSerializer
    filterset_class = PokemonItemFilter
