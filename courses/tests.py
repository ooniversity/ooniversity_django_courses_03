from django.test import TestCase

from courses.models import Course


class CourseTests(TestCase):
    def test_course_create(self):
        self.assertEqual(Course.objects.all().count(), 1)

    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa')
