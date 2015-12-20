from django.test import TestCase
from courses.models import Course, Lesson
import coaches.models
from django.contrib.auth.models import User
from django.test import Client



def obj_create():
    user_1 = User.objects.create(
        username='user_1')

    user_2 = User.objects.create(
        username='user_2')

    user_3 = User.objects.create(
        username='user_3')

    coach_1 = coaches.models.Coach.objects.create(
        user=user_1,
        date_of_birth='1977-04-01',
        gender='M',
        phone='(098) 224-24-24',
        address='Address1',
        skype='user_1',
        description='Coach1 description')

    coach_2 = coaches.models.Coach.objects.create(
        user=user_2,
        date_of_birth='1978-04-01',
        gender='M',
        phone='(098) 225-25-25',
        address='Address2',
        skype='user_2',
        description='Coach2 description')

    coach_3 = coaches.models.Coach.objects.create(
        user=user_3,
        date_of_birth='1979-04-01',
        gender='F',
        phone='(098) 226-26-26',
        address='Address3',
        skype='user_3',
        description='Coach3 description')

    course_1 = Course.objects.create(
        name='PyBursa03',
        short_description="Web development with Django",
        description="Description, PyBursa03",
        coach=coach_1, assistant=coach_3)

    course_2 = Course.objects.create(
        name='JavaBursa03',
        short_description="Java development",
        description="Description, JavaBursa03",
        coach=coach_1, assistant=coach_2)

    course_3 = Course.objects.create(
        name='BasicBursa02',
        short_description="Basic development",
        description="Description, BasicBursa02",
        coach=coach_3, assistant=coach_2)

    lesson_1_1 = Lesson.objects.create(
        subject='Variables and Types',
        description='Variables and Types...',
        course=course_1, order=1)

    lesson_1_2 = Lesson.objects.create(
        subject='Lists',
        description='Lists...',
        course=course_1, order=2)

    lesson_1_3 = Lesson.objects.create(
        subject='Basic Operators',
        description='Basic Operators...',
        course=course_1, order=3)


class CoursesListTest(TestCase):
    def test_index_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_index_courses_count(self):
        obj_create()
        self.assertEqual(Course.objects.all().count(), 3)

    def test_index_course_name_contains(self):
        client = Client()
        obj_create()
        response = client.get('/')
        self.assertContains(response, 'PYBURSA03')

    def test_index_course_descr_contains(self):
        client = Client()
        obj_create()
        response = client.get('/')
        self.assertContains(response, 'Web Development With Django')




class CoursesDetailTest(TestCase):
    def test_course_detail(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        obj_create()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail_template(self):
        client = Client()
        obj_create()
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_course_detail_contains(self):
        client = Client()
        obj_create()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Description, PyBursa03')

    def test_lessons_in_course_count(self):
        obj_create()
        self.assertEqual(Lesson.objects.all().count(), 3)

    def test_lesson_in_course_contain(self):
        client = Client()
        obj_create()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Variables and Types...')
