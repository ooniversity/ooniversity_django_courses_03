from datetime import date
from django.contrib.auth.models import User
from pybursa.views import index
from courses.views import CourseDetailView
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach


def create_courses():
    first_user = User.objects.create(username = 'first_user')
    second_user = User.objects.create(username = 'second_user')
    
    first_coach = Coach.objects.create(user=first_user, 
								       date_of_birth=date.today(),
								       gender='M',
								       phone='0000000000000000',
								       address='addddr',
								       skype='skype',
								       description='descr')
    
    second_coach = Coach.objects.create(user=second_user, 
								       date_of_birth=date.today(),
								       gender='M',
								       phone='0000000000000000',
								       address='addddr',
								       skype='skype',
								       description='descr')

    first_course = Course.objects.create(name='first_course', 
								         short_description='descr',
								         description='descr',
								         coach=first_coach,
								         assistant=second_coach)
    
    second_course = Course.objects.create(name='second_course', 
								         short_description='descr',
								         description='descr',
								         coach=first_coach,
								         assistant=second_coach)
    


class CoursesListTest(TestCase):

    def test_index_page(self):
        self.assertEqual(resolve('/').func, index)

    def test_index_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_html_content(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '<h2>PyBursa</h2>')

    def test_index_context(self):
        client = Client()
        create_courses()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['courses']), 2)

    def test_edit_course_url(self):
        client = Client()
        create_courses()
        response = client.get('/')
        for i in xrange(1, 3):
            self.assertContains(response, 'href="/courses/edit/{}/"'.format(i))

    def test_delete_course_url(self):
        client = Client()
        create_courses()
        response = client.get('/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/courses/remove/{}/"'.format(i))

    def test_add_course_url(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'href="/courses/add/"')



class CoursesDetailTest(TestCase):

    def test_detail_template(self):
        create_courses()
        for i in range(1, 3):
            self.assertEqual(resolve('/courses/{}/'.format(i)).func.__name__, 
                					 CourseDetailView.as_view().__name__)

    def test_404_course(self):
        client = Client()
        response = client.get(reverse('courses:detail', args=(1, )))
        self.assertEqual(response.status_code, 404)

    def test_index(self):
        create_courses()
        client = Client()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertEqual(response.status_code, 200)

    def test_detail_content(self):
        client = Client()
        create_courses()
        response = client.get(reverse('courses:detail', args=(1,)))
        self.assertTemplateUsed(response, 'courses/detail.html')
        self.assertContains(response, '<h3>Coach</h3>')

    def test_detail_context(self):
        client = Client()
        create_courses()
        response = client.get(reverse('courses:detail', args=(1,)))
        course = response.context['course']
        self.assertEqual(course.name, 'first_course')

    def test_add_lesson_url(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/courses/{}/add_lesson"'.format(i))

    def test_to_coach_url(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/coaches/1/"')

    def test_to_assistant_url(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/coaches/2/"')


       