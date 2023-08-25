# Generated by Django 3.2.12 on 2023-08-25 23:24
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0001_initial"),
        ("pokemon", "0002_rename_surname_pokemon_nickname"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="favorite_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="item.pokemonitem",
            ),
        ),
    ]
