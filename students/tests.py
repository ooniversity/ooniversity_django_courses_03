from django.test import TestCase
from students.models import Student
from django.test.client import Client

class StudentsDetailTest(TestCase):
	
	def test_student_create(self):
		kolst = Student.objects.all().count()
		st1 = Student.objects.create(
							name='himen',date_of_birth = '2014-12-10')
		self.assertEqual(Student.objects.all().count(), kolst+1) 

	def test_student_date_of_birth(self):
		for i in Student.objects.all():
			self.name.assertNotEqual(i.date_of_birth, '')

	def test__isupper(self):
		st1 = Student.objects.create(
							name='HIMEN',date_of_birth = '2014-12-10')
		self.assertTrue(st1.name.isupper())
		
	def test_pages(self):
		client = Client()
		responce = client.get('/testStudent')
		self.assertEqual(responce.status_code, 404)

	def test_None(self):
		st1 = Student.objects.create(
							name='himen',date_of_birth = '2014-12-10')
		self.assertIsNotNone(st1, None)
