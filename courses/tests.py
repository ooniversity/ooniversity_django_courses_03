from django.test import TestCase
from courses.models import Course, Lesson
from django.test import Client
from django.contrib.auth.models import User
from coaches.models import Coach


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

		
class CoursesDetailTest(TestCase):
	def test_page(self):
		client = Client()
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)
	def test_create_page(self):
		client = Client()	
		course1 = Course.objects.create(name="Python")
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
	def test_heder_page(self):
		client = Client()	
		course1 = Course.objects.create(name="Python")
		response = client.get('/courses/1/')
		self.assertContains(response,"Python")
	def test_detail_redirect(self):
		client = Client()
		course1 = Course.objects.create(name="Python")
		responce = client.get('/courses/1')
		self.assertEqual(responce.status_code, 301)
	def test_create_coach(self):
		client = Client()
		Coach.objects.create(
			user = User.objects.create_user(
				username = 'aaa_',
				password = '1',
				email = 'aaa@gmail.com',
				first_name = 'aaa',
				last_name = 'bbb',
				),
			date_of_birth = '2015-05-01',
			gender = 'M',
			phone = '1234657980',
			address = 'Kharkov',
			skype = 'aaa',
			description = 'coach',
			)
		responce = client.get('/')
		self.assertEqual(responce.status_code, 200)
	


		
		
		

