from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase, Client

from coaches.models import Coach
from courses.models import Course


def create_cours():
    user1 = User.objects.create(
        username='alex'
    )
    user2 = User.objects.create(
        username='alex'
    )
    coach_1 = Coach.objects.create(
        user=user1,
        date_of_birth=date.today(),
        gender='M',
        phone='555555',
        address='test address',
        skype='skype',
        description='description'
    )
    coach_2 = Coach.objects.create(
        user=user2,
        date_of_birth=date.today(),
        gender='F',
        phone='7777777',
        address='test address',
        skype='test',
        description='description'
    )
    course1 = Course.objects.create(
        name='course1',
        short_description='short descript',
        description='descripp',
        coach=coach_1,
        assistant=coach_2
    )
    course2 = Course.objects.create(
        name='course2',
        short_description='short descrip',
        description='descript',
        coach=coach_1,
        assistant=coach_2
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

    def test_valid_course_name_edit(self):
        client = Client()
        create_cours()
        response = client.get('/courses/edit/1/')
        self.assertContains(response, 'Cours')

    def test_link_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_link_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_link_feedback(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):
    def test_course_link(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_empty(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_create(self):
        create_cours()
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_create_less(self):
        client = Client()
        response = client.get('/courses/1/add_lesson')
        self.assertEqual(response.status_code, 200)

    def test_link_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_link_students(self):
        response = self.client.get('/students/', {'course_id': 1})
        self.assertEqual(response.status_code, 200)

    def test_link_feedback(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

    def test_edit_course(self):
        client = Client()
        create_cours()
        response = client.post('/courses/edit/1/', {
            'name': 'Course1_1',
            'short_description': 'SomeDescription_1',
            'description': 'SomeBigDescription_1'})
        self.assertEqual(response.status_code, 302)

    def test_course_template(self):
        client = Client()
        create_cours()
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')
