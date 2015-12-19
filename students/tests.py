# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course


def create_student():
    
    course01 = Course.objects.create(
        name='Python',
        short_description='The way of force',
        description='Придётся выживать',)

    course02 = Course.objects.create(
        name='Ruby',
        short_description='Keep calm and learn Ruby',
        description='Keep calm and learn Ruby',)

    student01 = Student.objects.create(
        name='name01',
        surname='surname01',
        date_of_birth='2000-01-01',
        email='email01@test.com',
        phone='066-666-66-66',
        address='Харьков',
        skype='skype01')

    student01.courses.add(course01)

    student02 = Student.objects.create(
        name='name02',
        surname='surname02',
        date_of_birth='2001-02-02',
        email='email02@test.com',
        phone='000-999-99-99',
        address='Донецк',
        skype='skype02',)

    student02.courses.add(course02)

class StudentsListTest(TestCase):

    def setUp(self):
        self.client = Client()
        create_student()

    def test_create_student(self):
        self.assertEqual(Student.objects.all().count(), 2)

    def test_edit_student(self):
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'name01')

    def test_student_list_template(self):
        client = Client()
        create_student()
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_title(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertContains(response, 'Students List')  

    def test_student_list_200(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

class StudentsDetailTest(TestCase):

    def setUp(self):
        self.client = Client()
        create_student()

    def test_detail_name(self):
        client = Client()
        create_student()
        response = self.client.get('/students/1/')        
        self.assertContains(response, '1')

    def test_student_html01(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '<td>Email</td>')

    def test_student_html02(self):
        response = self.client.get('/students/2/')
        self.assertContains(response, '<li class=""><a href="/feedback/">Feedback</a></li>')

    def test_student_skype(self):
        client = Client()
        create_student()
        response = self.client.get('/students/1/')  

    def test_student_surname(self):
        client = Client()
        create_student()
        response = self.client.get('/students/2/') 
