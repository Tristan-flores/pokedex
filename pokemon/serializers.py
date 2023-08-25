from rest_framework import serializers

from .models import Pokemon
from authentication.serializers import UserSerializer
from item.serializers import PokemonItemSerializer
from pokedex.serializers import PokedexCreatureDetailSerializer


class PokemonSerializer(serializers.ModelSerializer):
    """Serializer of Pokemon object"""

    favorite_item = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "pokedex_creature",
            "trainer",
            "nickname",
            "level",
            "experience",
            "favorite_item",
        )
        read_only_fields = ("id", "level")

    def get_favorite_item(self, instance):
        if instance.favorite_item:
            return PokemonItemSerializer(instance.favorite_item).data
        return None

    def validate(self, attrs):
        """Add pokemon nickname if no nickname is given"""
        nickname = attrs.get("nickname")
        pokedex_creature = attrs.get("pokedex_creature")
        if not nickname:
            attrs["nickname"] = pokedex_creature.name

        return super().validate(attrs)


class PokemonDetailsSerializer(serializers.ModelSerializer):
    pokedex_creature = PokedexCreatureDetailSerializer()
    trainer = UserSerializer()

    favorite_item = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "nickname",
            "level",
            "experience",
            "pokedex_creature",
            "trainer",
            "favorite_item",
        )

    def get_favorite_item(self, instance):
        if instance.favorite_item:
            return PokemonItemSerializer(instance.favorite_item).data
        return None


class PokemonGiveXPSerializer(serializers.Serializer):
    """Serializer of give-xp endpoint"""

    amount = serializers.IntegerField(min_value=0)
