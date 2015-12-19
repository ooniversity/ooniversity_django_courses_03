from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from datetime import date
from django.contrib.auth.models import User

def create_data_course():

    user1 = User.objects.create(
        username = 'Vasya'
    )

    coach1 = Coach.objects.create(
        user = user1,
        date_of_birth = date.today(),
        gender = 'M',
        phone = '123-123-123',
        address = 'address',
        skype = 'skype',
        description = 'description coach'
    )

    course1 = Course.objects.create(
        name = 'course1',
        short_description = 'short_description',
        description = 'description course',
        coach = coach1,
        assistant = coach1
    )

class CoursesListTest(TestCase):

    def test_course_link(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_course_data1(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', short_description='Text of perl.')
        response = client.get('/')
        self.assertContains(response, 'PERL')

    def test_course_data2(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', short_description='Text of perl.')
        response = client.get('/')
        self.assertContains(response, 'Text Of Perl.')

    def test_course_data3(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', short_description='Text of perl.')
        response = client.get('/')
        self.assertContains(response, 'ItBursa')

class CoursesDetailTest(TestCase):

    def test_course_link(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', description='Text of perl.')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_data1(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', description='Text of perl.')
        response = client.get('/courses/1/')
        self.assertContains(response, 'Perl')

    def test_course_data2(self):
        client = Client()
        course1 = Course.objects.create(name='Perl', description='Text of perl.')
        response = client.get('/courses/1/')
        self.assertContains(response, 'Text of perl.')

    def test_course_data3(self):
        client = Client()
        create_data_course()
        course1 = Course.objects.create()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_data4(self):
        client = Client()
        create_data_course()
        course1 = Course.objects.create()
        response = client.get('/courses/1/')
        self.assertContains(response, 'course1')
