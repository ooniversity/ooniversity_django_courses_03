from django.test import TestCase
from django.test import Client

from students.models import Student
from courses.models import Course

class StudentsListTest(TestCase):

	def test_students(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

	def test_students_count(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)
		response = client.get('/students/')
		self.assertEqual(Course.objects.all().count(), 1)

	def test_students_name(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)
		response = client.get('/students/')
		self.assertContains(response, 'student')

	def test_student_course(self):
		client = Client()

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)
		response = client.get('/students/?course_id=1')  
		self.assertEqual(response.status_code, 200)

	def test_student_skype(self):
		client = Client()

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)
		response = client.get('/students/')  
		self.assertContains(response, 'Andreyko')


class StudentsDetailTest(TestCase):

	def test_student_empty(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

	def test_student_name(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Siroja')

	def test_student_email(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'testsiroja@gmail.com')

	def test_student_address(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Kharkiv')

	def test_student_skype(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Test',
			short_description = 'Test',
			description = 'Test')

		student = Student.objects.create(
			name = 'Siroja',
			surname = 'Andreyko',
			date_of_birth = '1999-01-08',
			email = 'testsiroja@gmail.com',
			phone = '88008080',
			address = 'Kharkiv',
			skype = 'Andreyko'
			)

		response = client.get('/students/1/')
		self.assertContains(response, 'Andreyko')



