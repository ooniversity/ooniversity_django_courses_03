from django.test import TestCase
from django.test import Client


class PybursaTest(TestCase):

    def test_admin_login(self):
        c = Client()
        response = c.login(username='admin', password='admin')
