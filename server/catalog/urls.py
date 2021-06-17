from django.urls import path

from .views import CarsView

urlpatterns = [
    path("cars/", CarsView.as_view()),
]
