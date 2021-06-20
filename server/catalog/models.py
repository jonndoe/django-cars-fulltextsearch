import uuid

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    variety = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    # Add a new search_vector field to catalog_car database table with a tsvector datatype.
    search_vector = SearchVectorField(null=True, blank=True)

    # Add a GIN index on the search_vector field to make queries much faster
    class Meta:
        indexes = [GinIndex(fields=["search_vector"], name="search_vector_index")]

    def __str__(self):
        return f"{self.id}"


class SearchHeadline(models.Func):
    function = 'ts_headline'
    _output_field = models.TextField()
    template = '%(function)s(%(expressions)s, \'StartSel = <mark>, StopSel = </mark>, HighlightAll=TRUE\')'
