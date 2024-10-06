from django.test import TestCase

from ..helpers.testing import bordered, enable_output, disable_output

class DjangoTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        bordered('setUpTestData')

    def setUp(self):
        bordered('setUp')
    
    def test1(self):
        bordered('test1')
    
    def test2(self):
        bordered('test2')
