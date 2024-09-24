from django.test import TestCase
import json
# Create your tests here.

from ..models import MenuItems
from ..helpers.testing import bordered, enable_output, disable_output


class MenuItemsTest(TestCase):

    def test_empty_menuitems(self):
        self.assertEqual(MenuItems.objects.count(), 0)

