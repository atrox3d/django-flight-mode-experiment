from django.test import TestCase
import json
import datetime
# Create your tests here.

from ..helpers.testing import (
    bordered, enable_output, disable_output, request2dict
)

from myapp.forms import LogForm
from myapp.models import Logger

class FormsTest(TestCase):

    def test_logger_get(self):
        self.response = self.client.get('/logger')
        self.assertEqual(self.response.status_code, 200)

    def test_logger_post(self):
        self.assertEqual(Logger.objects.count(), 0)

        data={
            'first_name': 'first',
            'last_name': 'last',
            'time_log': '11:11',
        }
        form = LogForm(data=data)
        self.assertTrue(form.is_valid())
        self.response = self.client.post(
                    '/logger',
                    data=data
        )
        self.assertEqual(self.response.status_code, 200)

        self.assertEqual(Logger.objects.count(), 1)
        log = Logger.objects.first()
        bordered(log.dict())

        self.assertEqual(log.first_name, 'first')
        self.assertEqual(log.last_name, 'last')
        self.assertEqual(log.time_log, datetime.time(11, 11))

