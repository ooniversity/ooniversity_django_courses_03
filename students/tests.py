# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course

def insert_student():

    new_course_1 = Course.objects.create(
                            name='Python/Django',
                            short_description='Python/Django course',
                            description='Course is about Django, a Web development framework that saves you time and makes Web development a joy.')

    new_course_2 = Course.objects.create(
                            name='JavaScript',
                            short_description='JavaScript course',
                            description='Learn javascript online and supercharge your web design with this Javascript for beginners training course.')

    new_course_3 = Course.objects.create(
                            name='Web-design',
                            short_description='Web Design & Development',
                            description='The Web Design & Development I curriculum is an introduction to the design, creation, and maintenance of web pages and websites. ')

    new_student_1 = Student.objects.create(
                            name='Test1',
                            surname='Test1',
                            date_of_birth='1990-01-01',
                            email='test1@test.com',
                            phone='0931556565',
                            address='USA',
                            skype='test1')
    new_student_1.courses.add(new_course_1)

    new_student_2 = Student.objects.create(
                            name='Test2',
                            surname='Test2',
                            date_of_birth='1990-01-01',
                            email='test2@test.com',
                            phone='0952411223',
                            address='USA',
                            skype='test2',)
    new_student_2.courses.add(new_course_2)

    new_student_3 = Student.objects.create(
                            name='Test3',
                            surname='Test3',
                            date_of_birth='1990-01-01',
                            email='test3@test.com',
                            phone='0978789564',
                            address='USA',
                            skype='test3',)
    new_student_3.courses.add(new_course_3)

# Create your tests here.
class StudentsListTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_student()

    def test_new_student(self):
        self.assertEqual(Student.objects.all().count(), 3)

    def test_page_student(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'USA')
        self.assertContains(response, 'Список всех студентов')
        self.assertContains(response, 'Фамилия и имя')
        self.assertContains(response, 'Адрес')
        self.assertContains(response, 'Skype')
        self.assertContains(response, 'Курсы')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_link_add_edit_remove_student(self):
        response = self.client.get('/students/')
        self.assertContains(response, '/students/add/')
        for i in range(1, 3):
            self.assertContains(response, '/students/{}/'.format(i))
            self.assertContains(response, '/students/edit/{}/'.format(i))
            self.assertContains(response, '/students/remove/{}/'.format(i))
            self.assertContains(response, '/courses/{}/'.format(i))
            response2 = self.client.get('/students/', {'page': i})
            self.assertEqual(response2.status_code, 200)

    def test_check_valid_add_student(self):
        response = self.client.get('/students/add/')
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Surname')
        self.assertContains(response, 'Date of birth')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Phone')
        self.assertContains(response, 'Address')
        self.assertContains(response, 'Skype')
        self.assertContains(response, 'Courses')
        response = self.client.post('/students/add/')
        self.assertEqual(response.status_code, 200)

    def test_check_valid_edit_student(self):
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'Test1')
        self.assertContains(response, '0931556565')

    def test_check_valid_remove_student(self):
        for i in range(1, 3):
            response = self.client.post('/students/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 302)
            response = self.client.get('/students/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 404)

class StudentsDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_student()

    def test_detail_page_student(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_mail_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'test1@test.com')

    def test_course_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Python/Django')
        self.assertContains(response, '/courses/1/')

    def test_skype_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'test1')

    def test_phone_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '0931556565')
