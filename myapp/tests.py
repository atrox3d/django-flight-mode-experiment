from django.test import TestCase

# Create your tests here.

#  from .models import
from .helpers.testing import bordered

class TestUrls(TestCase):

    def test_home(self):
        response = self.client.get('/')
        bordered(response)