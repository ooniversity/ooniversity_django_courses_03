from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from courses.models import Course


class CoursesListTest(TestCase):

    def test_list(self):
        client = Client()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'Welcome to ITBursa-2015!')

    def test_course_create(self):
		course1 = Course.objects.create(name='ITBursa-2015', short_description='Welcome to ITBursa-2015!')
		self.assertEqual(Course.objects.all().count(), 1)

    def test_index_link(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

    def test_contacts_link(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        
    def test_feedback_link(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)        