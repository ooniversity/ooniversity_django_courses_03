from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course


class StudentsListTest(TestCase):
    def test_code_response(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200, 'Code response not valid')

    def test_empty_main_page(self):
        client = Client()
        response = client.get('/students/')
        students = response.context['object_list']
        self.assertEqual(len(students), 0, 'Main page has non reqiured element')

    def test_count_elements_main_page(self):
        client = Client()
        Student.objects.create(date_of_birth='2000-10-10')
        response = client.get('/students/')
        count = response.context['object_list']
        self.assertEqual(len(count), 1, 'Main page has non reqiured element')

    def test_required_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.templates[0].name, 'students/student_list.html', 'Invalid template for student list')

    def test_student_name(self):
        client = Client()
        Student.objects.create(name="student_name", date_of_birth='2000-10-10')
        response = client.get('/students/')
        name = response.context['object_list'][0].name
        self.assertEqual(name, 'student_name', 'Invalid student name')


class StudentsDetailTest(TestCase):

    def test_code_response(self):
        client = Client()
        Student.objects.create(name="student_name", date_of_birth='2000-10-10')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200, 'Code response not valid')

    def test_student_name(self):
        client = Client()
        Student.objects.create(name="student_name", date_of_birth='2000-10-10')
        response = client.get('/students/1/')
        self.assertEqual(response.context['student'].name, 'student_name', 'Invalid student name')

    def test_student_surname(self):
        client = Client()
        Student.objects.create(surname="student_surname", date_of_birth='2070-10-10')
        response = client.get('/students/1/')
        self.assertEqual(response.context['student'].surname, 'student_surname', 'Invalid student surname')

    def test_student_course_name(self):
        client = Client()
        student = Student(name="student_name", date_of_birth='2070-10-10')
        student.save()
        course = Course(name='Course name')
        course.save()
        student.courses.add(course)
        response = client.get('/students/1/')
        self.assertContains(response, 'Course name')

    def test_student_full_name(self):
        client = Client()
        student = Student(name="Name", surname='Surname', date_of_birth='2070-10-10')
        student.save()
        response = client.get('/students/1/')
        self.assertEqual(response.context['student'].full_name, 'Name Surname', 'Invalid student fullname')

