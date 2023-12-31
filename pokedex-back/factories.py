from random import randint
from random import sample

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from pytest_factoryboy import register

from item.models import PokemonItem
from pokedex.models import PokedexCreature
from pokemon.models import Pokemon

User = get_user_model()
DEFAULT_PASSWORD = "secretpassword"


class ItemFactory(DjangoModelFactory):
    """Generator of Item objects"""

    class Meta:
        model = PokemonItem

    name = factory.Sequence(lambda n: f"Item {n + 1}")
    image = "https://www.example.com/item_image.png"
    description = "Item description"


class PokedexCreatureFactory(DjangoModelFactory):
    """Generator of PokedexCreature objects"""

    class Meta:
        model = PokedexCreature

    name = factory.Sequence(lambda n: f"Creature {n + 1}")
    ref_number = randint(1, 750)
    type_1 = sample(["Poison", "Flying", "Dragon"], 1)
    type_2 = sample(["Fire", "Grass", None], 1)
    total = randint(100, 999)
    hp = randint(40, 200)
    attack = randint(40, 200)
    defense = randint(40, 200)
    special_attack = randint(40, 200)
    special_defence = randint(40, 200)
    speed = randint(40, 200)
    generation = randint(1, 9)
    legendary = False


class PokemonFactory(DjangoModelFactory):
    """Generator of PokedexCreature objects"""

    class Meta:
        model = Pokemon

    pokedex_creature = factory.SubFactory(PokedexCreatureFactory)
    level = 1
    experience = 0
    favorite_item = factory.LazyFunction(PokemonItem.objects.order_by("?").first)

    @factory.post_generation
    def clean(obj, create, extracted, **kwargs):
        """Call pokemon model clean method"""
        obj.clean()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username_{0}".format(n))
    email = factory.Sequence(lambda n: "user{0}@gmail.com".format(n))

    @factory.post_generation
    def set_password(obj, create, extracted, **kwargs):
        obj.set_password(DEFAULT_PASSWORD)
        obj.save()


register(PokedexCreatureFactory)
register(PokemonFactory)
register(UserFactory)
register(ItemFactory)
