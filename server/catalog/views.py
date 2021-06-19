from rest_framework.generics import ListAPIView

from .filters import CarFilterSet
from .models import Car
from .serializers import CarSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilterSet
