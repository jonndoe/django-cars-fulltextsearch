from django_filters.rest_framework import CharFilter, FilterSet

from .models import Car, CarSearchWord


class CarFilterSet(FilterSet):
    query = CharFilter(method="filter_query")

    def filter_query(self, queryset, name, value):
        return queryset.search(value)

    class Meta:
        model = Car
        fields = (
            "query",
            "country",
            "points",
        )


class CarSearchWordFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        return queryset.search(value)

    class Meta:
        model = CarSearchWord
        fields = ('query',)
