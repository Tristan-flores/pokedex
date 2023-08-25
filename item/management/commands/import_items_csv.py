import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import PokemonItem


class Command(BaseCommand):
    """
    Import PokemonItem from CSV file
    """

    help = "Import items from CSV file and create PokemonItem instances"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file_path",
            type=str,
            nargs="?",
            default=os.path.join(settings.BASE_DIR, "liste_objets_pokemon.csv"),
        )

    def handle(self, *args, **options):
        csv_file_path = options.get("csv_file_path", None)
        if csv_file_path and csv_file_path.endswith(".csv"):
            with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                # Skip headers
                next(reader, None)

                items = [
                    PokemonItem(
                        name=row[0],
                        image_link=row[1],
                        description=row[2],
                    )
                    for row in reader
                ]

                PokemonItem.objects.bulk_create(
                    items,
                    batch_size=100,
                    # ignore_conflicts=True,
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Nb of items imported to the database: " f"{len(items)}."
                )
            )
        else:
            self.stderr.write(self.style.ERROR("This is not a CSV file."))
