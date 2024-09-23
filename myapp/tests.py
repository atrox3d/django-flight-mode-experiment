from django.test import TestCase
import json
# Create your tests here.

#  from .models import
from .helpers.testing import bordered

class TestHomeUrl(TestCase):
        
        # @classmethod
        # def setUpClass(cls) -> None:

        @classmethod
        def setUpClass(cls) -> None:
            super().setUpClass()
            cls.home = '/'
            cls.prefixed = '/home/'
            cls.urls = [cls.home, cls.prefixed] + 'fail these onws'.split()

        # def setUp(self):
            # self.home = '/'
            # self.prefix_home = '/home/'

        def test_subtest(self):
             for url in self.urls:
                  with self.subTest(url=url, msg='hellooo'):
                    self.response = self.client.get(url)
                    self.assertEqual(self.response.status_code, 200)
                       

        def test_home(self):
            self.response = self.client.get(self.home)
            self.assertEqual(self.response.status_code, 200)
        
        def test_hello(self):
            self.response = self.client.get(self.home)
            self.assertEqual(self.response.status_code, 200)

            self.assertContains(self.response, 'hello')
            self.assertEqual(self.response.content, b'hello')
        