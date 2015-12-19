from django.test import TestCase
from courses.models import Course


class CoursesListTest(TestCase):

    def test_students_list(self):
        course = Course.objects.create(
            name = 'Course',
            short_description = 'testCourse',
            description = 'testCourseDescription',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Course")


class CoursesDetailTest(TestCase):

    def test_students_list(self):
        course = Course.objects.create(
            name = 'Course',
            short_description = 'testCourse',
            description = 'testCourseDescription',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/courses/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Course")

