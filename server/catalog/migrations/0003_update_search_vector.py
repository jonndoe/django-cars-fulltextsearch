from django.contrib.postgres.search import SearchVector
from django.db import migrations


def update_search_vector(apps, schema_editor):
    Car = apps.get_model("catalog", "Car")
    Car.objects.all().update(
        search_vector=(
            SearchVector("variety", weight="A")
            + SearchVector("model", weight="A")
            + SearchVector("description", weight="B")
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_search_vector"),
    ]

    # The elidable argument tells Django to ignore
    # that operation when it squashes migrations.
    operations = [
        migrations.RunPython(update_search_vector, elidable=True),
    ]
