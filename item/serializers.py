from rest_framework import serializers

from .models import PokemonItem


class PokemonItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonItem
        fields = "__all__"
        read_only_fields = ("id",)
