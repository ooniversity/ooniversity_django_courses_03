# -*- coding: utf-8 -*- 
from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

class CoursesListTest(TestCase):

    def test_course_create(self):
        course_py = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django")
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_list(self):
        client = Client()
        course_py = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django")
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PYTHON BURSA")
    
    def test_python_delete(self):
      course_py = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django")
      response = self.client.get('/courses/remove/1/')
      self.assertEqual(response.status_code, 200)

    def test_python_update(self):
      course_py = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django")
      response = self.client.get('/courses/edit/1/')
      self.assertEqual(response.status_code, 200)

    def test_new_course(self):
      response = self.client.get('/courses/add/')
      self.assertEqual(response.status_code, 200)

    
class CoursesDetailTest(TestCase):
    
    def test_course_detail(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
                                    name="Python Bursa", 
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django")
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Bursa")


    def test_coach_detail(self):
        coach_obj = Coach.objects.create( 
                                    user=User.objects.create(),
								    date_of_birth='1869-01-21',
								    gender='M',
								    phone='06718690121',
								    address='Российская Империя, Петроград',
								    skype='RasPutin69',
								    description = 'some descr')
        course_obj = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django",
                                    description="some descr",
                                    coach=coach_obj,
                                    assistant=coach_obj)
        response = self.client.get("/courses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Bursa")

    def test_add_lesson(self):
        client = Client()
        response = client.get('/courses/1/add_lesson')
        self.assertEqual(response.status_code, 200)

    def test_assistant_detail(self):
        assistant_obj = Coach.objects.create( 
                                    user=User.objects.create(),
								    date_of_birth='1552-02-21',
								    gender='M',
								    phone="06715520221",
								    address="Российская Империя, Москва",
								    skype="God52",
								    description = "some descr")
        course_obj = Course.objects.create(
                                    name="Python Bursa",
                                    short_description="Основы Языка Программирования Python + Web Разработка На Django",
                                    description="some descr",
                                    coach=assistant_obj,
                                    assistant=assistant_obj)
        response = self.client.get("/courses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Bursa")

    def test_coach_detail_link(self):
        client = Client()
        coach_obj = Coach.objects.create( 
                                    user=User.objects.create(),
								    date_of_birth='1869-01-21',
								    gender='M',
								    phone='06718690121',
								    address='Российская Империя, Петроград',
								    skype='RasPutin69',
								    description = 'some descr')
        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)





