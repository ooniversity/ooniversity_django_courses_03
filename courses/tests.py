from django.test import TestCase
from courses.models import Course


class CoursesListTest(TestCase):

    def test_course_list(self):
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

    def test_course_detail(self):
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


class CoursesDeleteTest(TestCase):

    def test_course_delete(self):
        course = Course.objects.create(
            name = 'Course',
            short_description = 'testCourse',
            description = 'testCourseDescription',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/courses/remove/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Course remove")


class CoursesEditTest(TestCase):

    def test_course_edit(self):
        course = Course.objects.create(
            name = 'Course',
            short_description = 'testCourse',
            description = 'testCourseDescription',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/courses/edit/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Course Edit")


class CoursesAddTest(TestCase):

    def test_course_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/courses/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Create new Course")

