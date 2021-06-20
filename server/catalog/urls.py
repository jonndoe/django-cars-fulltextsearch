from django.urls import path

from .views import CarsView, CarSearchWordsView

urlpatterns = [
    path("cars/", CarsView.as_view()),
    path("car-search-words/", CarSearchWordsView.as_view()),
]
