from rest_framework.generics import ListAPIView

from .filters import CarFilterSet, CarSearchWordFilterSet
from .models import Car, CarSearchWord
from .serializers import CarSerializer, CarSearchWordSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilterSet


class CarSearchWordsView(ListAPIView):
    queryset = CarSearchWord.objects.all()
    serializer_class = CarSearchWordSerializer
    filterset_class = CarSearchWordFilterSet
