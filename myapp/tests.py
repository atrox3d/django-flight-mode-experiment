from django.test import TestCase
import json
# Create your tests here.

#  from .models import
from .helpers.testing import bordered

class TestHomeUrl(TestCase):
        
        @classmethod
        def setUpClass(cls) -> None:
            # AttributeError: django.test.TestCase has no attribute 'cls_atomics'
            super().setUpClass()
        
            cls.home = '/'
            cls.prefixed = '/home/'
            cls.urls = (
                [cls.home, cls.prefixed]
                + 'fail1 fail2 fail3'.split()
            )

        def test_subtest(self):
            for url in self.urls:
                with self.subTest(url=url, msg=f'hellooo {url}'):
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
        