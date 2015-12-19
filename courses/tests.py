from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client


class CoursesListTest(TestCase):
    def test_course_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_cource_fail(self):
        from django.test import Client
        client = Client()

        response = client.get('cources/1/')
        self.assertEqual(response.status_code, 404)

        course1 = Course.objects.create(
                                        name = "qwerty",
                                        short_description = "qwerty",
                                        description = "qwerty",
                                        )
        response = client.get('/course/1/')
