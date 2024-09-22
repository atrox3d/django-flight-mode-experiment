from django.test import TestCase
import json
# Create your tests here.

#  from .models import
from .helpers.testing import bordered

class TestHomeUrl(TestCase):

        # def setUp(self):
        #     self.response = self.client.get('/')
        #     self.assertEqual(self.response.status_code, 200)

        def test_home(self):
            self.response = self.client.get('/')
            self.assertEqual(self.response.status_code, 200)
        
        def test_hello(self):
            self.response = self.client.get('/')
            self.assertEqual(self.response.status_code, 200)

            self.assertContains(self.response, 'hello')
            self.assertEqual(self.response.content, b'hello')
        