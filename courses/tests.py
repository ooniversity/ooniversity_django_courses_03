# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client


def insert_course():
    new_user_1 = User.objects.create(
                            username='user_1')

    new_user_2 = User.objects.create(
                            username='user_2')

    new_user_3 = User.objects.create(
                            username='user_3')

    new_coach_1 = Coach.objects.create(
                            user=new_user_1,
	                        date_of_birth='1985-12-30',
	                        gender='M',
	                        phone='000-666-66-66',
	                        address='Kiev, Ukraine',
	                        skype='user_1',
	                        description='The Assistant at the 2nd and the 3d courses.')
    
    new_coach_2 = Coach.objects.create(
                            user=new_user_2,
	                        date_of_birth='1985-12-30',
	                        gender='M',
	                        phone='000-666-66-66',
	                        address='Kiev, Ukraine',
	                        skype='user_1',
	                        description='The Assistant at the 2nd and the 3d courses.')
    
    new_coach_3 = Coach.objects.create(
                            user=new_user_3,
	                        date_of_birth='1985-12-30',
	                        gender='M',
	                        phone='000-666-66-66',
	                        address='Kiev, Ukraine',
	                        skype='user_1',
	                        description='The Assistant at the 2nd and the 3d courses.')


    new_course_1 = Course.objects.create(
                            name='Python/Django',
                            short_description='Практический курс',
                            description='Практический курс по изучению современного языка программирования Python и фреимворка Django.',
                            coach=new_coach_1,
                            assistant=new_coach_3)

    new_course_2 = Course.objects.create(
                            name='JS',
                            short_description='JavaScript',
                            description='прототипно-ориентированный сценарный язык программирования.',
                            coach=new_coach_1,
                            assistant=new_coach_2)

    new_course_3 = Course.objects.create(
                            name='Symphony',
                            short_description='Symphony.',
                            description='Синтаксис, подходы, философия, инструменты и экосистема..',
                            coach=new_coach_3,
                            assistant=new_coach_2)


  

# Create your tests here.
class CoursesListTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_course()

    def test_new_course(self):
        self.assertEqual(Course.objects.all().count(), 3)

    def test_page_course(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PYTHON/DJANGO')
        self.assertTemplateUsed(response, 'index.html')
    
    def test_link_add_edit_remove_course(self):
        response = self.client.get('/')
        self.assertContains(response, '/courses/add/')
        for i in range(1, 4):
            self.assertContains(response, '/courses/edit/{}/'.format(i))
            self.assertContains(response, '/courses/remove/{}/'.format(i))
    
    def test_check_valid_add_course(self):
        response = self.client.get('/courses/add/')
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Short description')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Coach')
        self.assertContains(response, 'Assistant')
    
    def test_check_valid_edit_course(self):
        response = self.client.get('/courses/edit/1/')
        self.assertContains(response, 'user_1')
        self.assertContains(response, 'user_3')
    
    def test_check_valid_remove_course(self):
        for i in range(1, 4):
            response = self.client.post('/courses/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 302)
            response = self.client.get('/courses/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 404)
    

class CoursesDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_course()

    def test_detail_page_course(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Практический курс')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_link_student(self):
        response = self.client.get('/students/', {'course_id': 1})
        self.assertEqual(response.status_code, 200)

    def test_coach(self):
        response = self.client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)

    def test_add_lesson(self):
        response = self.client.get('/courses/1/add_lesson')
        self.assertContains(response, 'Subject')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Course')
        self.assertContains(response, 'Order')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/courses/1/add_lesson', {'subject': 'test', 'description': 'test', 'course': 'Python/Django', 'order': 4})
        self.assertEqual(response.status_code, 200)

    def test_check_coache(self):
        response = self.client.get('/courses/1/')
        self.assertContains(response, '/coaches/1/')
        
        


