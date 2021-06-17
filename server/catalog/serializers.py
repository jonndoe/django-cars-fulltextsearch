from rest_framework import serializers

from .models import Car


# This code tells the server how to serialize a Car resource
# from a database record to a JSON string
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            "id",
            "country",
            "description",
            "points",
            "price",
            "variety",
            "model",
        )
