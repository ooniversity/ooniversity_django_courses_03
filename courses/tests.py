from django.test import TestCase, Client
from courses.models import Course

class CoursesListTest(TestCase):

	def setUp(self):
		self.client = Client()	

	def test_list_create(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		self.assertEqual(Course.objects.all().count(), 1)

	
	def test_list_delete(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		course1.delete()
		self.assertEqual(Course.objects.all().count(), 0)


	def test_list_update(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		course1.short_description ="New description"
		course1.save()
		response = self.client.get('/')
		self.assertContains(response, "New")


	def test_main(self):
		course1 = Course.objects.create(
			name="MIT",
			short_description="Test description")
		response = self.client.get('/')
		self.assertContains(response, "MIT")


	def test_attribute(self):
		course1 = Course.objects.create(name='Harvard')
		self.assertTrue(course1.name)
	
	
class CoursesDetailTest(TestCase):

	def setUp(self):
		self.client = Client()	

	def test_200_status(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)


	def test_non_existent_page(self):
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)


	def test_detail_create(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		response = self.client.get('/courses/1/')
		self.assertContains(response, "Test")


	def test_template_used(self):
		course1 = Course.objects.create(
			name="Test",
			short_description="Test description")
		with self.assertTemplateUsed('courses/detail.html'):
			self.client.get('/courses/1/')


	def test_detail_view(self):
		course1 = Course.objects.create(
			name="MIT",
			short_description="Test description")
		response = self.client.get('/courses/1/')
		self.assertContains(response, "MIT")