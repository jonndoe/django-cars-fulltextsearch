from rest_framework import serializers

from .models import Car


# This code tells the server how to serialize a Car resource
# from a database record to a JSON string
class CarSerializer(serializers.ModelSerializer):

    variety = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_variety(self, obj):
        if hasattr(obj, 'variety_headline'):
            return getattr(obj, 'variety_headline')
        return getattr(obj, 'variety')

    def get_model(self, obj):
        if hasattr(obj, 'model_headline'):
            return getattr(obj, 'model_headline')
        return getattr(obj, 'model')

    def get_description(self, obj):
        if hasattr(obj, 'description_headline'):
            return getattr(obj, 'description_headline')
        return getattr(obj, 'description')

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
