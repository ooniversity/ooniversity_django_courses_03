from django.test import TestCase
from students.models import Student
from django.test import Client


class StudentsListTest(TestCase):

	def test_student_create(self):
		student1 = Student.objects.create(name='Ivan', surname='Petrov', 
										date_of_birth='1989-12-16', email='my_tets@gmail.com', 
										phone='0345343333', address='In thee sky', skype='test')
		self.assertEqual(Student.objects.all().count(), 1)
		
	def test_list_page_student(self):
		client = Client()
		student1 = Student.objects.create(name='Ivan', surname='Petrov', 
										date_of_birth='1989-12-16', email='my_tets@gmail.com', 
										phone='0345343333', address='In thee sky', skype='test')
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Petrov')
		
	def test_contacts_link(self):
		response = self.client.get('/contact/')
		self.assertEqual(response.status_code, 200)
		
	def test_index_link(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	def test_feedback_link(self):
		response = self.client.get('/feedback/')
		self.assertEqual(response.status_code, 200)
		
		
class StudentsDetailTest(TestCase):

	def test_detail_page_student(self):
		client = Client()
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)
		student1 = Student.objects.create(name='Ivan', surname='Petrov', 
										date_of_birth='1989-12-16', email='my_tets@gmail.com', 
										phone='0345343333', address='In thee sky', skype='test')
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Ivan')
		
	def test_index_link(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	def test_contacts_link(self):
		response = self.client.get('/contact/')
		self.assertEqual(response.status_code, 200)
		
	def test_students_link(self):
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		
	def test_feedback_link(self):
		response = self.client.get('/feedback/')
		self.assertEqual(response.status_code, 200)
