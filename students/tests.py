from django.test import TestCase, Client

from courses.models import Course
from students.models import Student


def list_students():
    course1 = Course.objects.create(
        name='PyBursa',
        short_description='Web development with django',
        description='Web development with django about django'
    )
    course2 = Course.objects.create(
        name='PyBursa01',
        short_description='Web development with python',
        description='Web development with django python'
    )

    course3 = Course.objects.create(
        name='Html',
        short_description='Web development with Html',
        description='Web development with django Html'
    )
    new_student_1 = Student.objects.create(
        name='Test',
        surname='Surname',
        date_of_birth='1986-04-27',
        email='tt@gmail.com',
        phone='055-11-22',
        address='Test',
        skype='test')
    new_student_1.courses.add(course1)

    new_student_2 = Student.objects.create(
        name='Test1',
        surname='Surname',
        date_of_birth='1988-09-20',
        email='tttn@gmail.com',
        phone='055-882-7774',
        address='ta',
        skype='test2')
    new_student_2.courses.add(course2)

    new_student_3 = Student.objects.create(
        name='Test5',
        surname='Surname1',
        date_of_birth='1985-06-24',
        email='pk@gmail.com',
        phone='0554-886-7774',
        address='TTTT',
        skype='sk')
    new_student_3.courses.add(course3)


class StudentsListTest(TestCase):
    def test_student_list_and_tmpl(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_list_code(self):
        client = Client()
        list_students()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_link_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_link_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_list_template(self):
        client = Client()
        list_students()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_title(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Students')


class StudentsDetailTest(TestCase):
    def test_student_list_and_tmpl(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_list_code(self):
        client = Client()
        list_students()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_link_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_link_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        list_students()
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/students/edit/1/',
                                    {'name': 'PP',
                                     'surname': 'Sn',
                                     'date_of_birth': '1989-04-20',
                                     'email': 'Mp@gmail.com',
                                     'phone': '055987-88-777',
                                     'address': 'KK',
                                     'skype': 'skp'})
        self.assertEqual(response.status_code, 200)
