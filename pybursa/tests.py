from django.test import TestCase
from django.test import Client

class PybursaTest(TestCase):
    def test_admin_login(self):
        client = Client()
        response = client.login(username='admin', password='admin')
