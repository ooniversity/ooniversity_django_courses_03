from django.test import TestCase, Client
from courses.models import Course
from students.models import Student
from datetime import date
#from django.core.urlresolvers import resolve, reverse

def data_student():

    course1 = Course.objects.create(
        name = 'Perl',
        short_description = 'short_description',
        description = 'description',
    )

    student1 = Student.objects.create(
        name = 'Petr',
        surname = 'Ivanov',
        date_of_birth = '1977-07-07',
        email  = 'email@gmail.com',
        phone = '123-123-123',
        address = 'address',
        skype = 'student_skype',
    )
    student1.courses.add(course1)

class StudentsListTest(TestCase):

    def test_student_link(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_link2(self):
        client = Client()
        data_student()
        student = Student.objects.create(date_of_birth = '1977-07-07')
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_data1(self):
        client = Client()
        data_student()
        student = Student.objects.create(date_of_birth = '1977-07-07')
        response = client.get('/students/')
        self.assertContains(response, 'student_skype')

    def test_student_data2(self):
        client = Client()
        data_student()
        student = Student.objects.create(date_of_birth = '1977-07-07')
        response = client.get('/students/')
        self.assertContains(response, 'Ivanov')

class StudentsDetailTest(TestCase):

    def test_detail_link(self):
        client = Client()
        data_student()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_tamplate(self):
        client = Client()
        data_student()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_detail_data1(self):
        client = Client()
        data_student()
        response = client.get('/students/1/')
        self.assertContains(response, 'Petr')

    def test_detail_data2(self):
        client = Client()
        data_student()
        response = client.get('/students/1/')
        self.assertContains(response, 'Ivanov')

    def test_detail_data3(self):
        client = Client()
        data_student()
        response = client.get('/students/1/')
        self.assertContains(response, 'email@gmail.com')
