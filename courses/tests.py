from django.test import TestCase
from courses.models import Course


class CoursesListTest(TestCase):
	def test_course_create(self):
		course1 = Course.objects.create(name="Python")
		self.assertEqual(Course.objects.all().count(),1)
		
	def test_page(self):
		from django.test import Client
		client = Client()
		response = client.get('courses/1/')
		self.assertEqual(response.status_code, 404)
		course1 = Course.objects.create(name="Python")
		response = client.get('courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response,"Python")
		
		
		
		

