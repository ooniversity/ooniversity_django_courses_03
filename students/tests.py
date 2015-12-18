# -*- coding: utf-8 -*- 
from django.test import TestCase, Client
from students.models import Student
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User

class StudentsListTest(TestCase):

    def test_student_create(self):
        student_obj = Student.objects.create(
                                    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15" )
                                    
        self.assertEqual(Student.objects.all().count(), 1)

    def test_course_list(self):
        client = Client()
        student_obj = Student.objects.create(
                                    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15" )
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Кузнецов Андрей")
   
    def test_student_delete(self):
      student_obj = Student.objects.create(
                                    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15" )
      response = self.client.get('/students/remove/1/') 
      self.assertEqual(response.status_code, 200)

    def test_student_update(self):
      student_obj = Student.objects.create(
                                    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15" )
      response = self.client.get('/students/edit/1/') 
      self.assertEqual(response.status_code, 200)

    def test_new_student(self):
      response = self.client.get('/students/add/')
      self.assertEqual(response.status_code, 200)

    def test_student_detail_link(self):
        client = Client()
        student_obj = Student.objects.create( 
								    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15",
                                    phone="+380930157035")
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)


class StudentsDetailTest(TestCase):

    def test_student_detail(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student_obj = Student.objects.create(
                                    name="Кузнецов Андрей",
                                    skype="AlexK",
                                    address="Украина, Харьков",
                                    date_of_birth="1989-02-15",
                                    phone="+380930157035")
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Кузнецов Андрей")

    def test_courses_detail(self):
        client = Client()
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
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_link_students(self):
		client = Client()
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)
    
    def test_link_feedbacks(self):
		client = Client()
		response = client.get('/feedback/')
		self.assertEqual(response.status_code, 200)

    def test_link_index(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

    def test_link_contacts(self):
		client = Client()
		response = client.get('/contact/')
		self.assertEqual(response.status_code, 200)
