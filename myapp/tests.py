from django.test import TestCase

# Create your tests here.

#  from .models import

class TestUrls(TestCase):

    def test_home(self):
        response = self.client.get('/')
        print(response)