from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class SmokeTest(TestCase):
    def test_root(self):
        client = APIClient()
        resp = client.get('/api/')
        self.assertIn(resp.status_code, (200, 401))
