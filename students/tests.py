from django.test import TestCase, Client
from students.models import Student
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy

class StudentsListTest(TestCase):

    def test_student_create(self):
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        self.assertEqual(Student.objects.all().count(), 1)
    def test_list_statuscode(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertEqual(responce.status_code, 200)
    def test_list_url_active(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertContains(responce, '<li class="active"><a href="/students/">Students</a></li>')
    def test_list_header(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertContains(responce, 'Students')
    def test_create_content(self):
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'Katya')


class StudentsDetailTest(TestCase):
    def test_page(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_student_create(self):
        client = Client()
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response,"Python")

    def test_student_content(self):
        client = Client()
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        response = client.get('/students/1/')
        #self.assertEqual(response.status_code, 200)
        self.assertContains(response,"Katya")

    def test_detail_redirect(self):
        client = Client()
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        responce = client.get('/courses/1')
        self.assertEqual(responce.status_code, 301)

    def test_student_date_of_birth(self):
        client = Client()
        student1 = Student.objects.create(name="Katya",date_of_birth = '1990-09-10')
        response = client.get('/students/1/')
        self.assertContains(response,'Sept. 10, 1990')
