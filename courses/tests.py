from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client


class CoursesListTest(TestCase):

    def test_course_list(self):
        #self.client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 0) 
        coach1=Coach.objects.create(
            user=User.objects.create(),
            date_of_birth='1980-01-01',
            gender='F',
            phone='0-800-345-657-765',
            address='City',
            skype='SomeSkype',
            description='SomeDescription') 
        course1 = Course.objects.create(
            name='SomeCourse',
            short_description='SomeDescription',
            description='SomeBigDescription',
            coach=coach1,
            assistant=coach1)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SomeDescription')
        self.assertEqual(Course.objects.all().count(), 1)
            
class CoursesDetailTest(TestCase):

    def test_course_create(self):
    
        coach1=Coach.objects.create(
            user=User.objects.create(),
            date_of_birth='1980-01-01',
            gender='F',
            phone='0-800-345-657-765',
            address='City',
            skype='SomeSkype',
            description='SomeDescription')
            
        #coach2=Coach.objects.create(
            #user=User.objects.create(),
            #date_of_birth='1981-01-01',
            #gender='M',
            #phone='0-800-345-657-745',
           # address='Town',
            #skype='SomeSkype2',
            #description='SomeDescription2')
            
        course1 = Course.objects.create(
            name='SomeCourse',
            short_description='SomeDescription',
            description='SomeBigDescription',
            coach=coach1,
            assistant=coach1)
            
        self.assertEqual(Course.objects.all().count(), 1)  
    def test_course_detail(self):
         self.client = Client()
         response = self.client.get('/courses/1/')
         self.assertEqual(response.status_code, 404)
         self.assertEqual(Course.objects.all().count(), 0) 
         coach1=Coach.objects.create(
            user=User.objects.create(),
            date_of_birth='1980-01-01',
            gender='F',
            phone='0-800-345-657-765',
            address='City',
            skype='SomeSkype',
            description='SomeDescription') 
         course1 = Course.objects.create(
            name='SomeCourse',
            short_description='SomeDescription',
            description='SomeBigDescription',
            coach=coach1,
            assistant=coach1)
         response = self.client.get('/courses/1/')
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'SomeCourse')
         self.assertEqual(Course.objects.all().count(), 1)
    def test_course_edit(self):
        coach1=Coach.objects.create(
            user=User.objects.create(),
            date_of_birth='1980-01-01',
            gender='F',
            phone='0-800-345-657-765',
            address='City',
            skype='SomeSkype',
            description='SomeDescription') 
        course1 = Course.objects.create(
            name='SomeCourse',
            short_description='SomeDescription',
            description='SomeBigDescription',
            coach=coach1,
            assistant=coach1)
        response = self.client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/courses/edit/1/', {'name': 'Course1_1', 'short_description': 'SomeDescription_1', 'description': 'SomeBigDescription_1'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/courses/1/')
        #self.assertContains(response, 'SomeBigDescription_1')
         
# Create your tests here.
