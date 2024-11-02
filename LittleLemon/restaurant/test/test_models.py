from django.test import TestCase
from LittleLemon.restaurant.models import Menu

class MenuTest(TestCase):
    def test_str(self):
        item = Menu.objects.create(title="IceCream", price=80, description="Delicious")
        self.assertEqual(str(item), "IceCream : 80")