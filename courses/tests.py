from django.test import TestCase
from django.test import Client
from models import Course
from coaches.models import Coach
from django.contrib.auth.models import User


class CoursesListTest(TestCase):

    def test_code_response(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200, 'Code response not valid')

    def test_empty_main_page(self):
        client = Client()
        response = client.get('')
        c = response.context['items']
        self.assertEqual(len(c), 0, 'Main page has non reqiured element')

    def test_count_elements_main_page(self):
        client = Client()
        Course.objects.create(name="course_name")
        response = client.get('')
        count = response.context['items']
        self.assertEqual(len(count), 1, 'Main page has non reqiured element')

    def test_required_template(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.templates[0].name, 'index.html', 'Invalid templates for main page')

    def test_course_name(self):
        client = Client()
        Course.objects.create(name="course_name")
        response = client.get('')
        name = response.context['items'][0].name
        self.assertEqual(name, 'course_name', 'Invalid course name')


class CoursesDetailTest(TestCase):

    def test_code_response(self):
        client = Client()
        Course.objects.create(name="course_name")
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200, 'Code response not valid')

    def test_course_name(self):
        client = Client()
        Course.objects.create(name="course_name")
        response = client.get('/courses/1/')
        self.assertEqual(response.context['item'].name, 'course_name', 'Invalid course name')

    def test_course_description(self):
        client = Client()
        Course.objects.create(name="course_name", description='course_description')
        response = client.get('/courses/1/')
        self.assertEqual(response.context['item'].description, 'course_description', 'Invalid course description')

    def test_course_coach_name(self):
        client = Client()
        user = User(first_name='First Name', last_name='Last Name', id=1)
        user.save()
        coach = Coach.objects.create(user=user, date_of_birth='2011-11-11')
        coach.save()
        Course.objects.create(name="course_name", description='course_description', coach=coach)
        response = client.get('/courses/1/')
        self.assertEqual(response.context['item'].coach.name, 'First Name', 'Invalid coach name')

    def test_course_coach_last_name(self):
        client = Client()
        user = User(first_name='First Name', last_name='Last Name', id=1)
        user.save()
        coach = Coach.objects.create(user=user, date_of_birth='2011-11-11')
        coach.save()
        Course.objects.create(name="course_name", description='course_description', coach=coach)
        response = client.get('/courses/1/')
        self.assertEqual(response.context['item'].coach.surname, 'Last Name', 'Invalid coach last name')




















