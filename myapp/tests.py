from django.test import TestCase
import json
# Create your tests here.

#  from .models import
from .helpers.testing import bordered

class TestUrls(TestCase):

    def test_home(self):
        response = self.client.get('/')
        bordered(f'{response.content.decode() = }')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'hello')