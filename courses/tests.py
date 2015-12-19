from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
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

class CoursesListTest(TestCase):

	def test_courses_response(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_courses_creation(self):
		course = course_creation()
		response = self.client.get('/')
		self.assertEqual(Course.objects.all().count(), 1)

	def test_courses_list_edit_link(self):
		course = course_creation()
		response = self.client.get('/courses/edit/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'courses/edit.html')

	def test_courses_remove_link(self):
		course = course_creation()
		response = self.client.post('/courses/remove/1/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/courses/remove/1/')
		self.assertEqual(response.status_code, 404)

	def test_courses_addition(self):
		course = course_creation()
		response = self.client.get('/')
		self.assertContains(response, 'TESTNAME')

class CourseDetailList(TestCase):


	def test_course_detail(self):
		course = course_creation()
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'courses/detail.html')

	def test_course_add_lesson(self):
		course = course_creation()
		response = self.client.get('/courses/1/add_lesson')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'courses/add_lesson.html')

	def test_course_view_content(self):
		course = course_creation()
		response = self.client.get('/coaches/1/')
		self.assertContains(response, course.coach.phone)
		self.assertEqual(response.status_code, 200)

	def test_course_view_after_additing_course(self):
		course = course_creation()
		lesson = Lesson.objects.create(subject = 'testlessonsubject',
										description = 'testlessondescription',
										course = course,
										order = 1)
		response = self.client.get('/courses/1/')
		self.assertContains(response, 'testlessonsubject')

#	def test_course_student_link(self):
#		course = course_creation
#		response = self.client.get('/students/', {'course_id': 1})
#		self.assertEqual(response.status_code, 200)
