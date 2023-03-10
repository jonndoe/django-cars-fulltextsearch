# Generated by Django 3.1.4 on 2021-06-17 14:06

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("country", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("points", models.IntegerField()),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("variety", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
            ],
        ),
    ]
