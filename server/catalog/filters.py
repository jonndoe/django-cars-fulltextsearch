from django_filters.rest_framework import CharFilter, FilterSet

from .models import Car


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
