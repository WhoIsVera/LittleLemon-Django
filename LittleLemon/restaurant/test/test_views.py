from django.test import TestCase
from rest_framework.test import APIClient
from LittleLemon.restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, description="Delicious")

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)