#-*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson


class CoursesListTest(TestCase):

	def test_list1(self):
		from django.test import Client
		client = Client()

		response = client.get('/')
		self.assertEqual(response.status_code, 200)

		course_one = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')		
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(), 1)


	def test_list2(self):
		from django.test import Client
		client = Client()

		response = client.get('/')
		self.assertEqual(response.status_code, 200)

		course_first = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'name')

	def test_list3(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')

	def test_list4(self):
		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')
		response = self.client.get('/')
		self.assertContains(response, '/courses/edit/{}/'.format(course.id))

	def test_list5(self):
		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')
		response = self.client.get('/')
		self.assertContains(response, '/courses/remove/{}/'.format(course.id))


class CoursesDetailTest(TestCase):

	def test_some1(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)

	def test_some2(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, course.name)

	def test_some3(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

	def test_some4(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, course.description)

	def test_some5(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Добавить занятие')