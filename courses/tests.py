from django.test import TestCase
from courses.models import Course
from django.test import Client

def createTestCourse(name,short_desc):
	return Course.objects.create(name=name, short_description=short_desc)

class CoursesListTest(TestCase):
	def test_courses_list(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_empty_courses(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, "<td>No students yet</td>")

	def test_courses_list_count(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/')
		self.assertEqual(len(response.context['courses_list']), 1)


	def test_courses_list_correct_name(self):
		client = Client()
		course = createTestCourse("Django", "best course")
		response = client.get('/')
		self.assertContains(response, course.name.upper())

	def test_courses_list_contains_description(self):
		client = Client()
		course = createTestCourse("Django", "best course")
		response = client.get('/')
		self.assertContains(response, "<td>%s</td>" % course.short_description.title())


class CoursesDetailTest(TestCase):
	def test_courses_detail(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/courses/%s/' % course.id)
		self.assertEqual(response.status_code, 200)

	def test_courses_detail_not_found(self):
			client = Client()
			response = client.get('/courses/54/')
			self.assertEqual(response.status_code, 404)

	def test_course_detail_page_correct_title(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/courses/%s/' % course.id)
		self.assertContains(response, "<title>Course detail</title>")

	def test_course_detail_page_correct_coaches(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/courses/%s/' % course.id)
		self.assertContains(response, "<p>No coaches yet</p>")

	def test_course_detail_page_correct_assistants(self):
		client = Client()
		course = Course.objects.create(name="Web dev", short_description="Best course")
		response = client.get('/courses/%s/' % course.id)
		self.assertContains(response, "<p>No assistants yet</p>")
