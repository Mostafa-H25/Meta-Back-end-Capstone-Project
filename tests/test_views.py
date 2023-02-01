from django.test import TestCase

from views import MenuItemsView
from models import Menu


class MenuViewTest(TestCase):
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items)