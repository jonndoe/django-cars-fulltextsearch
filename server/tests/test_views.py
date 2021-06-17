
from rest_framework.test import APIClient, APITestCase

from catalog.models import Car


class ViewTests(APITestCase):

    def test_empty_query_returns_everything(self):
        car = Car.objects.create(
            country='US',
            description='A hardcore car',
            points=90,
            price=100.00,
            variety='Sport coupe',
            model='Ford Mustang'
        )
        client = APIClient()
        response = client.get('/api/v1/catalog/cars/')
        self.assertJSONEqual(response.content, [{
            'country': 'US',
            'description': 'A hardcore car',
            'id': str(car.id),
            'points': 90,
            'price': '100.00',
            'variety': 'Sport coupe',
            'model': 'Ford Mustang',
        }])

