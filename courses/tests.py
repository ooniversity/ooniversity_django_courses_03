# -*- coding: utf-8 -*- 
from django.test import TestCase
from django.test import Client
from courses.models import Course
'''
class CoursesListTest(TestCase):
    def test_course_create(self):
        courseJava = Course.objects.create(
                                    name="LavaBursa",
                                     short_description="Основные Понятия Языка Программирования Java")
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_create(self):
        client = Client()
        courseJava = Course.objects.create(
                                    name="LavaBursa",
                                     short_description="Основные Понятия Языка Программирования Java")
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 200) 


class CoursesDetailTest(TestCase):
    def test_course_create(self):
        courseJava = Course.objects.create(
                                    name="LavaBursa",
                                    short_description="Основные Понятия Языка Программирования Java")
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_response(self):
        client = Client()
        courseJava = Course.objects.create(
                                    name="JavaBursa",
                                    short_description="Основные Понятия Языка Программирования Java")
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404) 
'''
