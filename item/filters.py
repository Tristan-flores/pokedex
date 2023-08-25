import django_filters

from .models import PokemonItem


class PokemonItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Name contains")
    description = django_filters.CharFilter(
        lookup_expr="icontains", label="Description contains"
    )

    class Meta:
        model = PokemonItem
        fields = ["name", "description"]
