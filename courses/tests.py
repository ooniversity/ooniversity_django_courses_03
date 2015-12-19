# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client

def course_create():

    coach01 = Coach.objects.create(
        user=User.objects.create(username='user01'),
        date_of_birth='2000-01-01',
        gender='M',
        phone='066-666-66-66',
        address='Харьков',
        skype='user01',
        description='TeamLead')
    
    coach02 = Coach.objects.create(
        user=User.objects.create(username='user02'),
        date_of_birth='2001-02-02',
        gender='F',
        phone='099-999-99-99',
        address='Донецк',
        skype='user02',
        description='TeamLead')

    course01 = Course.objects.create(
        name='Python',
        short_description='The way of force',
        description='Придётся выживать',
        coach=coach01,
        assistant=coach01)

    course02 = Course.objects.create(
        name='Ruby',
        short_description='Keep calm and learn Ruby',
        description='Keep calm and learn Ruby',
        coach=coach01,
        assistant=coach02)

class CourseTest(TestCase):

	def test_course_create(self):
		course1 = Course.objects.create(
			name='PyBursa01',
			short_description="Web development with django")
		self.assertEqual(Course.objects.all().count(), 1)

class CoursesListTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        course_create()

    def test_new_course(self):
        self.assertEqual(Course.objects.all().count(), 2)
    
    def test_course_add(self):
        response = self.client.get('/courses/add/')
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Short description')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Coach')
        self.assertContains(response, 'Assistant')

    def test_course_edit(self):
        response = self.client.get('/courses/edit/1/')
        self.assertContains(response, 'user01')
        self.assertContains(response, 'user02')

    def test_page_course(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PYTHON')
        self.assertTemplateUsed(response, 'index.html')

    def test_courses_links(self):
        response = self.client.get('/')
        self.assertContains(response, '/courses/add/')
        for i in range(1, 3):
            self.assertContains(response, '/courses/edit/{}/'.format(i))
            self.assertContains(response, '/courses/remove/{}/'.format(i))

class CoursesDetailTest(TestCase):

    def test_courses_links2(self):
		response = self.client.get('/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')

    def test_course_detail_view(self):
        client = Client()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_create(self):
        client = Client()
        course_create()
        self.assertEqual(Course.objects.all().count(), 2)

    def test_html01(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '<h3>Courses Program</h3>')

    def test_html02(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '<h4>Решайся, не пожалеешь</h4>')

    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')