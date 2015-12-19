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


    def test_course_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/courses/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Create new Course")

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

    def test_menu_main(self):
        from django.test import Client
        client = Client()
        respons = client.get('/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "List of courses")

class CoursesDetailTest(TestCase):

    def test_cs_detail(self):
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

    def test_cs_delete(self):
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

    def test_menu_contacts(self):
        from django.test import Client
        client = Client()
        respons = client.get('/contact/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Contacts")

    def test_cs_edit(self):
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


    def test_cs_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/courses/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Create new Course")

