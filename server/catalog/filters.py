from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from .models import Car


class CarFilterSet(FilterSet):
    query = CharFilter(method="filter_query")

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(variety__contains=value)
            | Q(model__contains=value)
            | Q(description__contains=value)
        )
        return queryset.filter(search_query)

    class Meta:
        model = Car
        fields = (
            "query",
            "country",
            "points",
        )
