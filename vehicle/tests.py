from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestcase(APITestCase):
    def setUp(self):
        pass

    # def test_create_car(self):
    #     """ Тестирование создания машины"""
    #
    #     data = {
    #         'title': 'test',
    #         'description': 'test description',
    #         'milage': []
    #     }
    #     response = self.client.post('/cars/', data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(
    #         response.json(),
    #         {'id': 1, 'last_milage': 0, 'usd_price': 0.0, 'milage': [], 'title': 'test',
    #          'description': 'test description', 'owner': None}
    #     )
    #     self.assertTrue(Car.objects.all().exists())
    #
    # def test_list_car(self):
    #     """ Тестирование вывода списка машин"""
    #
    #     Car.objects.create(
    #         title='list_test',
    #         description='list_test'
    #     )
    #     response = self.client.get('/cars/')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     self.assertEqual(response.json(),
    #                      [{'id': 2, 'last_milage': 0, 'milage': [], 'title': 'list_test', 'description': 'list_test',
    #                        'owner': None}]
    #                      )
