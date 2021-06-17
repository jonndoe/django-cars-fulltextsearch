
from rest_framework.generics import ListAPIView

from .models import Car
from .serializers import CarSerializer
from .filters import CarFilterSet


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilterSet