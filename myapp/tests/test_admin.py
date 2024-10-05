from django.contrib.auth.models import User
from django.test import TestCase
from pathlib import Path
import json

from ..helpers.testing import bordered, enable_output, disable_output
from fakedata.loader import load_from_json
# Create your tests here.

class AdminUserTest(TestCase):

    def test_query_users(self):
        self.assertEqual(User.objects.count(), 0)
        
        bordered(Path.cwd())
        ADMIN_JSON = Path.cwd() / 'fakedata/json/users.json'
        self.assertTrue(ADMIN_JSON.exists())

        adminjson = load_from_json(ADMIN_JSON)[0]
        bordered(json.dumps(adminjson, indent=2))

        User(**adminjson).save()
        self.assertEqual(User.objects.count(), 1)

