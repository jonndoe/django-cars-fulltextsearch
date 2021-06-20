from rest_framework.test import APIClient, APITestCase
from django.contrib.postgres.search import SearchVector

from catalog.models import Car, CarSearchWord
from catalog.serializers import CarSerializer


class ViewTests(APITestCase):
    fixtures = ["test_cars.json"]

    def setUp(self):
        Car.objects.all().update(search_vector=(
            SearchVector('variety', weight='A') +
            SearchVector('model', weight='A') +
            SearchVector('description', weight='B')
        ))

        self.client = APIClient()

    def test_empty_query_returns_everything(self):
        response = self.client.get("/api/v1/catalog/cars/")
        cars = Car.objects.all()
        self.assertJSONEqual(response.content, CarSerializer(cars, many=True).data)

    def test_query_matches_variety(self):
        response = self.client.get("/api/v1/catalog/cars/?query=sport")
        self.assertEquals(2, len(response.data))
        self.assertEquals(
            "000bbdff-30fc-4897-81c1-7947e11e6d1a", response.data[0]["id"]
        )

    def test_query_matches_model(self):
        response = self.client.get("/api/v1/catalog/cars/?query=Toyota")
        self.assertEquals(1, len(response.data))
        self.assertEquals(
            "21e40285-cec8-417c-9a26-4f6748b7fa3a", response.data[0]["id"]
        )

    def test_query_matches_description(self):
        response = self.client.get("/api/v1/catalog/cars/?query=car")
        self.assertEquals(4, len(response.data))
        self.assertCountEqual(
            [
                "58ba903f-85ff-45c2-9bac-6d0732544841",
                "21e40285-cec8-417c-9a26-4f6748b7fa3a",
                "0082f217-3300-405b-abc6-3adcbecffd67",
                "000bbdff-30fc-4897-81c1-7947e11e6d1a",
            ],
            [item["id"] for item in response.data],
        )

    def test_can_filter_on_country(self):
        response = self.client.get("/api/v1/catalog/cars/?country=France")
        self.assertEquals(2, len(response.data))
        self.assertEquals(
            "0082f217-3300-405b-abc6-3adcbecffd67", response.data[1]["id"]
        )
        self.assertEquals(
            "000bbdff-30fc-4897-81c1-7947e11e6d1a", response.data[0]["id"]
        )

    def test_can_filter_on_points(self):
        response = self.client.get("/api/v1/catalog/cars/?points=87")
        self.assertEquals(1, len(response.data))
        self.assertEquals(
            "21e40285-cec8-417c-9a26-4f6748b7fa3a", response.data[0]["id"]
        )

    def test_country_must_be_exact_match(self):
        response = self.client.get("/api/v1/catalog/cars/?country=Frances")
        self.assertEquals(0, len(response.data))
        self.assertJSONEqual(response.content, [])

    def test_search_results_returned_in_correct_order(self):
        response = self.client.get("/api/v1/catalog/cars/?query=Chardonnay")
        self.assertEquals(2, len(response.data))
        self.assertListEqual(
            [
                "0082f217-3300-405b-abc6-3adcbecffd67",
                "000bbdff-30fc-4897-81c1-7947e11e6d1a",
            ],
            [item["id"] for item in response.data],
        )

    def test_search_vector_populated_on_save(self):
        car = Car.objects.create(
            country='US',
            points=80,
            price=1.99,
            variety='Pinot Grigio',
            model='Charles Shaw'
        )
        car = Car.objects.get(id=car.id)
        print('--------------------', Car.search_vector)
        self.assertEqual("'charl':3A 'grigio':2A 'pinot':1A 'shaw':4A", car.search_vector)

    def test_description_highlights_matched_words(self):
        response = self.client.get('/api/v1/catalog/cars/?query=car')
        self.assertEquals('A spicy, toasty, fruity <mark>car</mark>.', response.data[0]['description'])

    def test_car_search_words_populated_on_save(self):
        CarSearchWord.objects.all().delete()
        Car.objects.create(
            country='US',
            description='A cheap, but inoffensive car.',
            points=80,
            price=1.99,
            variety='Pinot Grigio',
            model='BMW m5'
        )
        car_search_words = CarSearchWord.objects.all().order_by('word').values_list('word', flat=True)
        self.assertListEqual([
            'a',
            'bmw',
            'but',
            'car',
            'cheap',
            'inoffensive',
            'm5',
        ], list(car_search_words))