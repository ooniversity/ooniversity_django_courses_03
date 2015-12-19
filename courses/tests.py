from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User


class CoursesListTest(TestCase):

    def test_courses_response_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_valid_course(self):
        response = self.client.get('/courses/add/')
        self.assertContains(response, 'Название курса')
        self.assertContains(response, 'Краткле описание')
        self.assertContains(response, 'Описание')
        self.assertContains(response, 'Coach')
        self.assertContains(response, 'Assistant')

    def test_edit_valid_course(self):
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
        )
        response = self.client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/edit.html')

    def test_remove_valid_course(self):
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
        )
        response = self.client.post('/courses/remove/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 404)


class CoursesDetailTest(TestCase):

    def test_response_404(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_response_200(self):
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
        )
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(course.pk, 1)
        self.assertContains(response, 'Python/Django 3 Поток')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_add_lesson(self):
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
        )
        lesson = Lesson.objects.create(subject='Основы Python', order=1, course=course)
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Основы Python')

    def test_coache(self):
        user = User.objects.create(username='FirstUser')
        coach = Coach.objects.create(
            user=user,
            date_of_birth='1950-10-23'
        )
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
            coach=coach,
        )
        response = self.client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coaches/detail.html')
