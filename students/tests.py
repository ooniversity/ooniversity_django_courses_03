# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course


def insert_student():
    new_course_1 = Course.objects.create(
        name='Web разработка на Python/Django',
        short_description='Python/Django',
        description='Практический курс по изучению современного языка программирования Python и фреимворка Django.')

    new_course_2 = Course.objects.create(
        name='JavaScript',
        short_description='about JavaScript',
        description='about JavaScript')

    new_course_3 = Course.objects.create(
        name='ruby',
        short_description='ruby основы',
        description='Курсы ruby предназначены для тех, кто хочет изучить, начиная от азов и до профессиональных возможностей, современный, востребованный и в то же время очень понятный язык программирования..')

    new_student_1 = Student.objects.create(
        name='Student_Test1',
        surname='Student_Test1',
        date_of_birth='1988-01-10',
        email='Student_Test1@gmail.com',
        phone='099-162-03-01',
        address='г.Харьков',
        skype='Student_Test1')
    new_student_1.courses.add(new_course_1)

    new_student_2 = Student.objects.create(
        name='Student_Test2',
        surname='Student_Test2',
        date_of_birth='1988-01-01',
        email='Student_Test2@gmail.com',
        phone='099-162-03-02',
        address='г.Харьков',
        skype='Student_Test2', )
    new_student_2.courses.add(new_course_2)

    new_student_3 = Student.objects.create(
        name='Student_Test3',
        surname='Student_Test3',
        date_of_birth='1988-01-06',
        email='Student_Test3@gmail.com',
        phone='099-162-03-03',
        address='г.Харьков',
        skype='Student_Test3', )
    new_student_3.courses.add(new_course_3)


class StudentsListTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_student()

    def test_new_student(self):
        self.assertEqual(Student.objects.all().count(), 3)

    def test_page_student(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'г.Харьков')
        self.assertContains(response, 'Список студентов')
        self.assertContains(response, 'фамилия имя')
        self.assertContains(response, 'фдрес')
        self.assertContains(response, 'skype')
        self.assertContains(response, 'курсы')
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
        self.assertContains(response, '099-162-03-01')

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

    def test_title_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '<title>Student_Test1 Student_Test1</title>')

    def test_h1_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '<h2 class="top1">Student_Test1 Student_Test1</h2>')

    def test_mail_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Student_Test1@gmail.com')

    def test_course_check_student(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Web разработка на Python/Django')
        self.assertContains(response, '/courses/1/')
