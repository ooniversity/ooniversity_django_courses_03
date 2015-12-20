from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

def create_coach():
    Coach.objects.create(
        user = User.objects.create_user(
            username = 'aaa_coach01',
            password = 'c0@cho1',
            email = 'aaa_coach01@coach.com',
            first_name = 'aaa_First',
            last_name = 'aaa_Second',
            ),
        date_of_birth = '2015-09-01',
        gender = 'M',
        phone = '1234657980',
        address = 'abc abc 123 abc',
        skype = 'aaa_coach_01',
        description = 'coach full and dummy description',
        )

def create_course():
    Course.objects.create(
        name = 'aaa_course_01',
        short_description = 'some dummy course description',
        description = 'course full description with blackjack and whores',
        coach = Coach.objects.get(id=1),
        assistant = Coach.objects.get(id=1),
        )

def create_lesson(lesson_id):
    Lesson.objects.create(
        subject = 'aaa_lesson_'+str(lesson_id),
        description = 'lesson detailed description with preferance and courtisans',
        order = lesson_id,
        course = Course.objects.get(id=1),
        )

def create_full_course():
    create_coach()
    create_course()
    for i in range(5):
        create_lesson(i)

class CoursesListTest(TestCase):

    def test_list_statuscode(self):
        client = Client()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)
        
    def test_list_header(self):
        client = Client()
        responce = client.get('/')
        self.assertContains(responce, 'Welcome to God\'s Bursa, lucky man!')

    def test_list_url_active(self):
        client = Client()
        responce = client.get('/')
        self.assertContains(responce, '<li class="active"><a href="/">Main</a></li>')

    def test_create_coach(self):
        client = Client()
        create_coach()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_course(self):
        client = Client()
        create_coach()
        create_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_lesson(self):
        client = Client()
        create_full_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_list_content(self):
        client = Client()
        create_full_course()
        responce = client.get('/')
        self.assertContains(responce, 'AAA_COURSE_01')


class CoursesDetailTest(TestCase):

    def test_create_coach(self):
        client = Client()
        create_coach()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_course(self):
        client = Client()
        create_coach()
        create_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_create_lesson(self):
        client = Client()
        create_full_course()
        responce = client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_detail_redirect(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1')
        self.assertEqual(responce.status_code, 301)

    def test_detail_statuscode(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertEqual(responce.status_code, 200)
        
    def test_detail_content_course(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertContains(responce, 'aaa_course_01')

    def test_detail_content_coach(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertContains(responce, 'aaa_First  aaa_Second')

    def test_detail_content_lessons(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertContains(responce, 'aaa_lesson_4')

