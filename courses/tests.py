#-*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson

class CoursesListTest(TestCase):

	def test_list(self):
		from django.test import Client
		client = Client()

		response = client.get('/')
		self.assertEqual(response.status_code, 200)

		course_first = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')

		course_second = Course.objects.create(
			name = 'Test Name 2',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(), 2)


	def test_list_name(self):
		from django.test import Client
		client = Client()

		response = client.get('/')
		self.assertEqual(response.status_code, 200)

		course_first = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'name')

	def test_link_add(self):
		response = self.client.get('/')
		self.assertContains(response, '/courses/add/')

	def test_link_edit(self):
		course = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')
		response = self.client.get('/')
		self.assertContains(response, '/courses/edit/{}/'.format(course.id))


class CoursesDetailTest(TestCase):

	def test_detail_item(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)

	def test_detail_name(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, course.name)

	def test_detail_empty(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

	def test_detail_description(self):
		from django.test import Client
		client = Client()

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test Name 1',
			short_description = 'First test for course list',
			description = 'This is course number one')

		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, course.description)