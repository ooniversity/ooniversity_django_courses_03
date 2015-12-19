from django.test import TestCase
from courses.models import Course, Lesson


# Create your tests here.
class CoursesListTest(TestCase):
    def test_course_create(self):
        course1 = Course.objects.create(
            name='C++',
            short_description='Test C++'
        )
        self.assertEqual(Course.objects.all().count(), 1)

    def test_page_courses_list(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
            name='Javascript',
            short_description='Test Javascript')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JAVASCRIPT")

    def test_page_courses_list_empty(self):
        from django.test import Client
        client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses are available.")

    def test_add_new_course_link_presence(self):
        from django.test import Client
        client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add a new course")

    def test_courses_list_short_description_title_all_capital_letters(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
            name='Python',
            short_description='Python is a beautiful language!')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Is A Beautiful Language!")


class CoursesDetailTest(TestCase):
    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

        course1 = Course.objects.create(
            name='C++',
            short_description='Test C++')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "C++")
        #self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_courses_detail_name_in_header(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name='Java',
            short_description='Test Java')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Java")

    def test_courses_detail_description_truncate_32(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name='Java',
            description='The basics of Java and also characters check!')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The basics of Java and also c...")

    def test_add_new_lesson_link_presence(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name='Java',
            short_description='Test Java')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add a new lesson")

    def test_courses_detail_lessons_list_empty(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name='Java',
            short_description='Test Java')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No lessons are available.")