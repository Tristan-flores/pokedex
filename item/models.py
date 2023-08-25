from django.db import models


class PokemonItem(models.Model):
    """creatureItem object"""

    name = models.CharField(max_length=100, unique=True)
    image_link = models.URLField()
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """Return item name"""
        return self.name
