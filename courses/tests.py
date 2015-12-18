# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

class CoursesListTest(TestCase):
	
	def test_course_create(self):
		course1 = Course.objects.create(name='PyBursa02', short_description='Web development with django')
		self.assertEqual(Course.objects.all().count(), 1)
		
	def test_list_page_course(self):
		client = Client()
		course1 = Course.objects.create(name='PyBursa02', short_description='Web development with django')
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'PYBURSA')
		
	def test_contacts_link(self):
		response = self.client.get('/contact/')
		self.assertEqual(response.status_code, 200)
		
	def test_students_link(self):
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		
	def test_feedback_link(self):
		response = self.client.get('/feedback/')
		self.assertEqual(response.status_code, 200)
		
	
class CoursesDetailTest(TestCase):

	def test_detail_page_course(self):
		client = Client()
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)
		course1 = Course.objects.create(name='PyBursa02', short_description='Web development with django')
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'PyBursa')
		
	def test_clesson_create(self):
		client = Client()
		response = client.get('/courses/1/add_lesson')
		self.assertEqual(response.status_code, 200)
		
	def test_index_link(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	def test_contacts_link(self):
		response = self.client.get('/contact/')
		self.assertEqual(response.status_code, 200)
		
	def test_students_link(self):
		response = self.client.get('/students/', {'course_id': 1})
		self.assertEqual(response.status_code, 200)
		
	def test_feedback_link(self):
		response = self.client.get('/feedback/')
		self.assertEqual(response.status_code, 200)
		
	def test_detail(self):
		coach1 = Coach.objects.create(
								user=User.objects.create(),
								date_of_birth='2055-02-15',
								gender='M',
								phone='1341234',
								address='address',
								skype='skype',
								description = 'desc')
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description',
								coach=coach1,
								assistant=coach1)
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Course1-name')
		
		def test_edit(self):
			coach1 = Coach.objects.create(
								user=User.objects.create(),
								date_of_birth='1989-12-15',
								gender='M',
								phone='4563456',
								address='address',
								skype='skype',
								description = 'desc')
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description',
								coach=coach1,
								assistant=coach1)
		response = self.client.get('/courses/edit/1/')
		self.assertEqual(response.status_code, 200)
		
		def test_course_detail_add_lesson_button(self):
		coach1 = Coach.objects.create(
								user=User.objects.create(),
								date_of_birth='2015-12-15',
								gender='M',
								phone='111-11-11',
								address='address',
								skype='skype',
								description = 'desc')
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description',
								coach=coach1,
								assistant=coach1)
		response = self.client.get('/courses/1/')
		self.assertContains(response, 'Добавить занятие')

		
		

