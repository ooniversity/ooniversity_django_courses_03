from django.test import TestCase
from courses.models import Course, Lesson
from django.test import Client


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

		
		

