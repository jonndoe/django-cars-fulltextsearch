import uuid

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVectorField, TrigramSimilarity
from django.db import models
from django.db.models import F, Q


class CarQuerySet(models.query.QuerySet):

    def search(self, query):
        search_query = Q(Q(search_vector=SearchQuery(query)))
        # return highlighted results
        return self.annotate(
            variety_headline=SearchHeadline(F('variety'), SearchQuery(query)),
            model_headline=SearchHeadline(F('model'), SearchQuery(query)),
            description_headline=SearchHeadline(F('description'), SearchQuery(query)),
            search_rank=SearchRank(F('search_vector'), SearchQuery(query))
        ).filter(search_query).order_by('-search_rank', 'id')


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

    objects = CarQuerySet.as_manager()

    # Add a GIN index on the search_vector field to make queries much faster
    class Meta:
        indexes = [GinIndex(fields=["search_vector"], name="search_vector_index")]

    def __str__(self):
        return f"{self.id}"


class SearchHeadline(models.Func):
    function = 'ts_headline'
    output_field = models.TextField()
    template = '%(function)s(%(expressions)s, \'StartSel = <mark>, StopSel = </mark>, HighlightAll=TRUE\')'


class CarSearchWordQuerySet(models.query.QuerySet):
    def search(self, query):
        return self.annotate(
            similarity=TrigramSimilarity('word', query)
        ).filter(similarity__gte=0.3).order_by('-similarity')


class CarSearchWord(models.Model):
    word = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.word
