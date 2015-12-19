from django.test import TestCase
from courses.models import Course, Lesson
import random
from django.http import HttpResponseRedirect, HttpResponse
from django.test.client import Client

class CoursesDetailTest(TestCase):

	def test_course_create(self):
		kolcourses = Course.objects.all().count()
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description='Web')
		self.assertEqual(Course.objects.all().count(), kolcourses+1) 
	
	def test__isupper(self):
		course1 = Course.objects.create(
							name='PYBURSA02',
							short_description='Web')
		self.assertTrue(course1.name.isupper())

	def test_course_name(self):
		for i in Course.objects.all():
			self.name.assertNotEqual(i.name, '')

	def test_pages(self):
		client = Client()
		responce = client.get('/test')
		self.assertEqual(responce.status_code, 404)

	def test_None(self):
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description='Web')
		self.assertIsNotNone(course1, None)


class CoursesListTest(TestCase):
	def test_course_create(self):
		course1 = Course.objects.create(name="Python")
		self.assertEqual(Course.objects.all().count(),1)
	def test_lessons_create(self):
		course1 = Course.objects.create(name="Python")
		lesson1 = Lesson.objects.create(subject="Les1",course=course1,description="xfvdvdfv", order = 1)
		n_lesson = Lesson.objects.filter(course_id=course1.id)
  		self.assertEqual(n_lesson.all().count(),1)
	def test_list_url_active(self):
		client = Client()
		responce = client.get('/')
		self.assertContains(responce, '<li class="active"><a href="/">Main</a></li>')
	def test_list_statuscode(self):
		client = Client()
		responce = client.get('/')
		self.assertEqual(responce.status_code, 200)
	def test_list_header(self):
		client = Client()
		responce = client.get('/')
		self.assertContains(responce, 'PyBursa')
