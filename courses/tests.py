from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User

courses = [('Python', 'Bla bla bla Python', 'Too many Bla bla bla Python', 'coach_1', 'coach_2'),
           ('Java', 'Bla bla bla Java', 'Too many Bla bla bla Java', 'coach_2', 'coach_1')]


def create_data():
    coach_1 = Coach.objects.create(
        user=User.objects.create(username='user1', first_name='Alex', last_name='Smith', email='alex@email.com'),
        date_of_birth='1982-01-26',
        gender='M',
        phone='+380 50 00 11 15',
        address='1, Street st.',
        skype='skype1',
        description='Main coach')

    coach_2 = Coach.objects.create(
        user=User.objects.create(username='user2', first_name='Bill', last_name='Clinton', email='bill@email.com'),
        date_of_birth='1983-01-26',
        gender='M',
        phone='+380 50 00 11 17',
        address='2, Street st.',
        skype='skype2',
        description='1th helper')

    courses = [('Python', 'Bla bla bla Python', 'Too many Bla bla bla Python', coach_1, coach_2),
               ('Java', 'Bla bla bla Java', 'Too many Bla bla bla Python', coach_2, coach_1)]

    for course in courses:
        Course.objects.create(name=course[0], short_description=course[1], description=course[2], coach=course[3],
                              assistant=course[4])


class CoursesListTest(TestCase):
    def setUp(self):
        self.client = Client()

        create_data()

    def test_course(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_course_name_upper(self):
        response = self.client.get('/')
        for i in courses:
            name = i[0].upper()
            self.assertContains(response, name)
        self.assertEquals(response.status_code, 200)

    def test_course_sd_tittle(self):
        response = self.client.get('/')
        for i in courses:
            name = i[1].title()
            self.assertContains(response, name)
        self.assertEquals(response.status_code, 200)

    def test_edit_course(self):
        response = self.client.get('/courses/edit/1/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'user1')

    def test_edit_procces(self):
        response = self.client.post('/courses/remove/1/')
        self.assertEquals(response.status_code, 302)


class CoursesDetailTest(TestCase):
    def setUp(self):
        self.client = Client()

        create_data()

    def test_detail_course(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_coach(self):
        response = self.client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)

    def test_add_lesson(self):
        response = self.client.post('/courses/2/add_lesson',
                                    {'subject': 'Lesson 1', 'description': 'First lesson', 'course': 'Java', 'order': 1})
        self.assertEqual(response.status_code, 200)

    def test_check_coache(self):
        response = self.client.get('/courses/1/')
        self.assertContains(response, '/coaches/1/')

    def test_redirect_for_student(self):
        response = self.client.get('/students/', {'course_id': 1})
        self.assertEqual(response.status_code, 200)
