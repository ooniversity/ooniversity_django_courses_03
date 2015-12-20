from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.test import Client
import coaches.models
from django.contrib.auth.models import User


def obj_create():

    user_1 = User.objects.create(
        username='user_1')

    user_2 = User.objects.create(
        username='user_2')

    user_3 = User.objects.create(
        username='user_3')

    coach_1 = coaches.models.Coach.objects.create(
        user=user_1,
        date_of_birth='1977-04-01',
        gender='M',
        phone='(098) 224-24-24',
        address='Address1',
        skype='user_1',
        description='Coach1 description')

    coach_2 = coaches.models.Coach.objects.create(
        user=user_2,
        date_of_birth='1978-04-01',
        gender='M',
        phone='(098) 225-25-25',
        address='Address2',
        skype='user_2',
        description='Coach2 description')

    coach_3 = coaches.models.Coach.objects.create(
        user=user_3,
        date_of_birth='1979-04-01',
        gender='F',
        phone='(098) 226-26-26',
        address='Address3',
        skype='user_3',
        description='Coach3 description')

    course_1 = Course.objects.create(
        name='PyBursa03',
        short_description="Web development with Django",
        description="Description, PyBursa03",
        coach=coach_1, assistant=coach_3)

    course_2 = Course.objects.create(
        name='JavaBursa03',
        short_description="Java development",
        description="Description, JavaBursa03",
        coach=coach_1, assistant=coach_2)

    course_3 = Course.objects.create(
        name='BasicBursa02',
        short_description="Basic development",
        description="Description, BasicBursa02",
        coach=coach_3, assistant=coach_2)

    student_1 = Student.objects.create(
        name='test_student_name_1',
        surname='test_student_surname_1',
        date_of_birth='1944-04-01',
        email='test_email_2@pybursa.com',
        phone='098-222-33-44',
        address='test_address_1',
        skype='test_skype_1')
    student_1.courses.add(course_1)
    student_1.courses.add(course_3)

    student_2 = Student.objects.create(
        name='test_student_name_2',
        surname='test_student_surname_2',
        date_of_birth='1945-04-01',
        email='test_email_2@pybursa.com',
        phone='097-234-56-78',
        address='test_address_2',
        skype='test_skype_2', )
    student_2.courses.add(course_2)
    student_2.courses.add(course_3)

    student_3 = Student.objects.create(
        name='test_student_name_3',
        surname='test_student_surname_3',
        date_of_birth='1902-04-01',
        email='test_email_3@pybursa.com',
        phone='096-222-22-22',
        address='test_address_3',
        skype='test_skype_3', )
    student_3.courses.add(course_1)
    student_3.courses.add(course_2)


class StudentsListTest(TestCase):
    def test_index_page(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_students_list_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_empty_students_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 0)


    def test_students_count(self):
        client = Client()
        obj_create()
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 3)

    def test_students_name_contains(self):
        client = Client()
        obj_create()
        response = client.get('/students/')
        self.assertContains(response, 'test_student_name_1')




class StudentsDetailTest(TestCase):
    def test_course_detail(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        obj_create()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_detail_template(self):
        client = Client()
        obj_create()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_student_detail_contains(self):
        client = Client()
        obj_create()
        response = client.get('/students/1/')
        self.assertContains(response, 'test_student_surname_1')

    def test_student_learn_first_course(self):
        client = Client()
        obj_create()
        response = client.get('/students/1/')
        self.assertContains(response, 'PyBursa03')

    def test_student_learn_second_course(self):
        client = Client()
        obj_create()
        response = client.get('/students/1/')
        self.assertContains(response, 'BasicBursa02')
