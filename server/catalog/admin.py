from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "country",
        "description",
        "points",
        "price",
        "variety",
        "model",
        "search_vector",
    )
    list_display = (
        "id",
        "country",
        "points",
        "price",
        "variety",
        "model",
    )
    list_filter = (
        "country",
        "variety",
        "model",
    )
    ordering = ("variety",)
    readonly_fields = ("id",)
