from django.test import TestCase
import json
# Create your tests here.

#  from .models import
from .helpers.testing import bordered, enable_output, disable_output

disable_output()

class TestHomeUrl(TestCase):
        
    @classmethod
    def setUpClass(cls) -> None:
        # AttributeError: django.test.TestCase has no attribute 'cls_atomics'
        super().setUpClass()
    
        cls.home = '/'
        cls.prefixed = '/home/'
        cls.urls = (
            [cls.home, cls.prefixed]
            # + 'fail1 fail2 fail3'.split()
        )

    def test_home_urls_200_subtests(self):
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

class RequestsURL(TestCase):
    
    urls = [
        '/requestjson',
        '/requesttext',
    ]

    def test_request_urls_200_subtests(self):
        for url in self.urls:
            with self.subTest(url=url, msg=f'hellooo {url}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)

class ResponseURL(TestCase):
    
    urls = [
        '/responsejson'
        # '/requesttext',
    ]

    def test_response_urls_200_subtests(self):
        for url in self.urls:
            with self.subTest(url=url, msg=f'hellooo {url}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)

class MenuItems(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dishes = 'pasta falafel cheesecake'.split()
        cls.urls = [f'/dishes/{dish}' for dish in cls.dishes]
        cls.elements = [
            # {'url': url, 'dish':dish} for url, dish in
            (url, dish) for url, dish in
            zip(cls.urls, cls.dishes)
        ]
        return super().setUpClass()

    def test_response_dishes_200_subtests(self):
        for url in self.urls:
            with self.subTest(url=url, msg=f'hellooo {url}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)

    def test_dishes_contains_dish_subtests(self):
        for url, dish in self.elements:
            with self.subTest(url=url, dish=dish, msg=f'hellooo {url, dish}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)
                self.assertContains(self.response, dish)
