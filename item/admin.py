from django.contrib import admin

from .models import PokemonItem


class CreatureItemAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in PokemonItem._meta.fields if field.name != "id"
    ]
    ordering = ("name",)
    search_fields = ("name",)
    list_per_page = 50


admin.site.register(PokemonItem, CreatureItemAdmin)
