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

class CoursesDetailTest(TestCase):
    def test_page(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_create(self):
        client = Client()
        course1 = Course.objects.create(name="Python")
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response,"Python")

    def test_course_content(self):
        client = Client()
        course1 = Course.objects.create(name="Python")
        response = client.get('/courses/1/')
        #self.assertEqual(response.status_code, 200)
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
                username = 'dvfsd',
                password = 'sdfsdf',
                email = 'sdfsd01@ffff.com',
                first_name = 'sdf',
                last_name = 'sfdsdf',
                ),
            date_of_birth = '2010-10-01',
            gender = 'F',
            phone = '1234657980',
            address = 'dgvsdv',
            skype = 'dfbfdb',
            description = 'dfbdf dfgvdfb dvfd',
            )
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)


