# Generated by Django 4.0.3 on 2022-03-04 13:52
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pokedex", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(blank=True, max_length=100, null=True)),
                ("level", models.PositiveSmallIntegerField(default=1)),
                ("experience", models.PositiveIntegerField(default=0)),
                (
                    "pokedex_creature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pokedex.pokedexcreature",
                    ),
                ),
                (
                    "trainer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
