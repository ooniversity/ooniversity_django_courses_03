from django.test import TestCase
from students.models import Student
from django.test import Client
import datetime
from django.core.urlresolvers import reverse
from courses.models import Course

def createTestCourse(name,short_desc):
	return Course.objects.create(name=name, short_description=short_desc)

def createTestStudent(name,surname,dob,email):
	return Student.objects.create(name=name,
										date_of_birth=dob,
										surname=surname,
										email=email,
										phone="2233322",
										skype="superuserdo")

class StudentsListTest(TestCase):
	def test_student_list(self):
		client = Client()
		createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		response = client.get(reverse('students:list_view'))
		self.assertEqual(response.status_code, 200)

	def test_student_list_count(self):
		client = Client()
		createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		response = client.get(reverse('students:list_view'))
		self.assertEqual(len(response.context['student_list']), 1)

	def test_student_courses_filtration(self):
		client = Client()
		student1 = createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		student2 = createTestStudent("john","johnson",datetime.date(1979,1,2),"fdsf@gmail.com")		
		course = createTestCourse("Web dev", "best course")
		student1.courses = [course]
		response = client.get(reverse('students:list_view'),{'course_id' : 1})
		self.assertEqual(len(response.context['student_list']), 1)

	def test_student_pagination(self):
		client = Client()
		student1 = createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		student2 = createTestStudent("john","johnson",datetime.date(1979,1,2),"fdsf@gmail.com")		
		student3 = createTestStudent("jack","jackson",datetime.date(1991,1,2),"fdsf@gmail.com")		

		response = client.get(reverse('students:list_view'))
		self.assertEqual(len(response.context['student_list']), 2)

	def test_student_list_pagination_error(self):
		client = Client()
		student1 = createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		response = client.get(reverse('students:list_view'), {'page' : 2})
		self.assertEqual(response.status_code, 404)

class StudentsDetailTest(TestCase):
	def test_student_detail(self):
		client = Client()
		st = createTestStudent("valera", "ivanoffF", datetime.date(1992,1,3), "asdf@gmail.com")
		response = client.get("/students/%s/" % st.id)
		self.assertEqual(response.status_code, 200)

	def test_student_detail_not_found(self):
		client = Client()
		response = client.get("/students/54/")
		self.assertEqual(response.status_code, 404)

	def test_student_detail_name(self):
		client = Client()
		st = createTestStudent("valera", "ivanoff", datetime.date(1992,1,3), "asdf@gmail.com")
		response = client.get("/students/%s/" % st.id)

		self.assertEqual(response.context['student'].full_name(), "valera ivanoff")

	def test_student_detail_page_correct_title(self):
		client = Client()
		st = createTestStudent("valera", "ivanoff", datetime.date(1992,1,14), "asdf@gmail.com")
		response = client.get("/students/%s/" % st.id)

		self.assertContains(response, "<title>Student detail</title>")

 	def test_student_detail_skype(self):
 		client = Client()
		st = createTestStudent("valera", "ivanoff", datetime.date(1992,1,14), "asdf@gmail.com")
		response = client.get('/students/%s/' % st.id)  
		self.assertContains(response, '<td>%s</td>' % "superuserdo" )

