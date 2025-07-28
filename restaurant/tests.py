from django.test import TestCase

# Create your tests here.
from .models import Menu


class MenuModelTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(name="Pasta", price=12.50)
        self.assertEqual(item.name, "Pasta")