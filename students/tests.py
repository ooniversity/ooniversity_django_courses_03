from django.test import TestCase, Client
from students.models import Student
from coaches.models import Coach
from django.contrib.auth.models import User
from courses.models import Course


class StudentsListTest(TestCase):

    def test_list(self):
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'Student\'s list:')

    def test_index_link(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

    def test_list_statuscode(self):
        client = Client()
        responce = client.get('/students/')
        self.assertEqual(responce.status_code, 200)

    def test_contacts_link(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)