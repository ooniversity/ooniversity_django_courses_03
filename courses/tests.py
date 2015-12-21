from django.test import TestCase
from courses.models import Course
from django.test import Client

class CoursesListTest(TestCase):
    def test_course_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail(self):
        response = self.client.get('courses/3/')
        self.assertEqual(response.status_code, 200)
