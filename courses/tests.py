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
        student1 = Course.objects.create(
            name='C++',
            short_description='Test C++')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "C++")

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
        student1 = Course.objects.create(
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