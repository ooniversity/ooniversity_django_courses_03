from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse

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
        description='Web development with django about python'
    )

    course3 = Course.objects.create(
        name='Html',
        short_description='Web development with Html',
        description='Web development with django about Html'
    )
    new_student_1 = Student.objects.create(
        name='Henry',
        surname='Surname',
        date_of_birth='1981-04-20',
        email='henry@gmail.com',
        phone='055-88-777',
        address='Petrovskogo',
        skype='henry')
    new_student_1.courses.add(course1)

    new_student_2 = Student.objects.create(
        name='Dan',
        surname='Surname',
        date_of_birth='1981-04-20',
        email='Dan@gmail.com',
        phone='055-88-777',
        address='Petrovskogo',
        skype='Dan')
    new_student_2.courses.add(course2)

    new_student_3 = Student.objects.create(
        name='Ran',
        surname='Surname',
        date_of_birth='1981-04-20',
        email='Ran@gmail.com',
        phone='055-88-777',
        address='Petrovskogo',
        skype='Ran')
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
        # self.assertTemplateUsed(response, 'students/student_list.html')

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
                                    {'name': 'Ran',
                                     'surname': 'Surname',
                                     'date_of_birth': '1981-04-20',
                                     'email': 'Ran@gmail.com',
                                     'phone': '055-88-777',
                                     'address': 'Petrovskogo',
                                     'skype': 'Ran'})
        self.assertEqual(response.status_code, 200)

    # def test_student_list_template(self):
    #     client = Client()
    #     list_students()
    #     response = client.get('/students/')
    #     self.assertTemplateUsed(response, 'students/student_detail.html')

    # def test_student_title(self):
    #     client = Client()
    #     response = client.get('/students/')
    #     self.assertContains(response, 'Students')
