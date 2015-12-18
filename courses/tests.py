from django.test import TestCase, Client
from courses.models import Course, Lesson


class CoursesListTest(TestCase):
    def test_list(self):
        client = Client()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'Welcome to ITBursa-2015!')