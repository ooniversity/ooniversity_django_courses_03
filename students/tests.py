from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from students.models import Student
from django.contrib.auth.models import User

def course_creation():
	test_user = User.objects.create(username = 'test')
	test_coach = Coach.objects.create(user = test_user, 
									date_of_birth = '1488-2-28',
									gender = 'F',
									phone = '12313213',
									address = 'testaddress',
									skype = 'skype',
									description = 'coach descr')
	course = Course.objects.create( name = 'TestName', 
									short_description = 'Test short short_description', 
									description = 'test discr'	,
									coach = test_coach, 
									assistant = test_coach)
	return course

def student_creation():
	course = course_creation()
	student = Student.objects.create(name = 'teststudent',
									surname = 'testsurname',
									date_of_birth = '1919-4-9',
									email = 'a@mail.ru',
									phone = '123456789',
									address = 'teststudentaddress',
									skype = 'studentskype',
									)
	student.courses.add(course)
	return student

class StudentsListTest(TestCase):

	def test_student_creation(self):
		student = student_creation()
		response = self.client.get('/students/')
		self.assertEqual(Student.objects.all().count(), 1)

	def test_students_list_response_and_template(self):
		student = student_creation()
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_list.html')

	def test_students_list_editing_link(self):
		student = student_creation()
		response = self.client.get('/students/edit/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_form.html')

	def test_students_remove_link(self):
		student = student_creation()
		response = self.client.post('/students/remove/1/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/students/remove/1/')
		self.assertEqual(response.status_code, 404)

	def test_students_addition(self):
		student = student_creation()
		response = self.client.get('/students/')
		self.assertContains(response, 'teststudent')

class StudentsDetailList(TestCase):

	def test_student_detail(self):
		student = student_creation()
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_detail.html')

	def test_student_detail_name(self):
		student = student_creation()
		response = self.client.get('/students/1/')
		self.assertContains(response, student.name)

	def test_student_link_to_course(self):
		student = student_creation()
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '/courses/1/')

	def test_student_detail_mail(self):
		student = student_creation()
		response = self.client.get('/students/1/')
		self.assertContains(response, student.email)

	def test_student_detail_skype(self):
		student = student_creation()
		response = self.client.get('/students/1/')
		self.assertContains(response, student.skype)	