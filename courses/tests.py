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