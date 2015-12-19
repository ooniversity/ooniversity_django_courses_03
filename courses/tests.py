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
                                        name = "vdv",
                                        short_description = "qwerty",
                                        description = "qwerty",
                                        )
        response = client.get('/course/1/')

    def test_create_coach(self):
        client = Client()
        create_coach()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_course_create(self):
        course_py = Course.objects.create(
                                    name="Basic Python",
                                    short_description="Python programming language")
        self.assertEqual(Course.objects.all().count(), 1)

    def test_new_course(self):
      response = self.client.get('/courses/add/')
      self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):

    def test_create_course(self):
        client = Client()
        create_coach()
        create_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_coach(self):
        client = Client()
        create_coach()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_lesson(self):
        client = Client()
        create_full_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_response_404(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


