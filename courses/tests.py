# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client


def insert_course():
    new_user_first = User.objects.create(
        username='user_first')

    new_user_second = User.objects.create(
        username='user_second')

    new_user_third = User.objects.create(
        username='user_third')

    new_coach_1 = Coach.objects.create(
        user=new_user_first,
        date_of_birth='1987-10-11',
        gender='F',
        phone='(099) 162-12-64',
        address='г.Харьков',
        skype='user_first',
        description='ассистент + тренер')

    new_coach_2 = Coach.objects.create(
        user=new_user_second,
        date_of_birth='1988-11-28',
        gender='M',
        phone='(099) 162-12-33',
        address='г.Харьков',
        skype='user_second',
        description='ассистент')

    new_coach_3 = Coach.objects.create(
        user=new_user_third,
        date_of_birth='1988-11-28',
        gender='M',
        phone='(099) 099-162-12-33',
        address='г.Харьков',
        skype='user_third',
        description='ассистент')

    new_course_1 = Course.objects.create(
        name='Python/Django',
        short_description='Web разработка на Python/Django',
        description='Курсы Python/Django предназначены для тех, кто хочет изучить, начиная от азов и до профессиональных возможностей, современный, востребованный и в то же время очень понятный язык программирования.',
        coach=new_coach_1,
        assistant=new_coach_3)

    new_course_2 = Course.objects.create(
        name='JavaScript',
        short_description='about JavaScript',
        description='about JavaScript.',
        coach=new_coach_1,
        assistant=new_coach_2)

    new_course_3 = Course.objects.create(
        name='ruby основы',
        short_description='ruby основы',
        description='Курсы ruby предназначены для тех, кто хочет изучить, начиная от азов и до профессиональных возможностей, современный, востребованный и в то же время очень понятный язык программирования.',
        coach=new_coach_3,
        assistant=new_coach_2)


class CoursesListTest(TestCase):
    def setUp(self):
        self.client = Client()
        insert_course()

    def test_new_course(self):
        self.assertEqual(Course.objects.all().count(), 3)

    def test_page_course(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Web разработка на Python/Django')
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
        response = self.client.post('/courses/1/add_lesson',
                                    {'subject': 'test', 'description': 'test', 'course': 'Web разработка на Python/Django', 'order': 4})
        self.assertEqual(response.status_code, 200)

    def test_check_coache(self):
        response = self.client.get('/courses/1/')
        self.assertContains(response, '/coaches/1/')
