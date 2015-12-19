#from django.test import TestCase
#from courses.models import Course
from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

class CoursesListTest(TestCase):

    def test_course_create(self):
        course = Course.objects.create(name="Python")
        self.assertEqual(Course.objects.all().count(), 1)

    def test_lessons_create(self):
        course1 = Course.objects.create(name="Python")
        lesson1 = Lesson.objects.create(subject="Les1",course=course1,description="xfvdvdfv", order = 1)
        course1_lessons = Lesson.objects.filter(course_id=course1.id)
        self.assertEqual(course1_lessons.all().count(),1)
    def test_list_statuscode(self):
        client = Client()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)
    def test_list_url_active(self):
        client = Client()
        responce = client.get('/')
        self.assertContains(responce, '<li class="active"><a href="/">Main</a></li>')
    def test_list_header(self):
        client = Client()
        responce = client.get('/')
        self.assertContains(responce, 'PyBursa')
