from django.test import TestCase, Client
from students.models import Student


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
		
	def test_create(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='234234',
								address='sun',
								skype='stud1')
		self.assertEqual(Student.objects.all().count(), 1)
		
		
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
		
	def test_detail(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='dfbsdf',
								address='sun',
								skype='stud1')
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, student1)
