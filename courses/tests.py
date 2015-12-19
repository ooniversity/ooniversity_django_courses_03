from django.test import TestCase, Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

def create_coach():
    Coach.objects.create(
        user = User.objects.create_user(
            username = 'test_coach',
            password = 'test_coach',
            email = 'test_coach@gmail.com',
            first_name = 'Test',
            last_name = 'Coach',
            ),
        date_of_birth = '1987-01-01',
        gender = 'M',
        phone = '0935735000',
        address = 'New_York',
        skype = 'test_coach',
        description = 'new test_coach',
        )

def create_course():
    Course.objects.create(
        name = 'test_course',
        short_description = 'new test_course in openstack',
        description = 'fuel and openstack',
        coach = Coach.objects.get(id=1),
        assistant = Coach.objects.get(id=1),
        )

def create_lesson(lesson_id):
    Lesson.objects.create(
        subject = 'test_lesson_'+str(lesson_id),
        description = 'New test_lesson',
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
        self.assertContains(responce, 'Start learn Linux and Openstack now!')

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
        self.assertContains(responce, 'test_course')

    def test_detail_content_coach(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertContains(responce, 'Test  Coach')

    def test_detail_content_lessons(self):
        create_full_course()
        client = Client()
        responce = client.get('/courses/1/')
        self.assertContains(responce, 'test_lesson_4')