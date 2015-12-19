from django.test import TestCase, Client
from students.models import Student


class StudentsListTest(TestCase):
    def test_list(self):
        client = Client()
        responce = client.get('/students/')
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'Student\'s list:')