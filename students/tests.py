from django.test import TestCase
from students.models import Student
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime
from django.test import Client

def add_student():
    coach1=Coach.objects.create(
        user=User.objects.create(username='root'),
        date_of_birth='1900-10-01',
        gender='M',
        phone='2132312',
        address='NY',
        skype='skype',
        description='description') 
    
    course1 = Course.objects.create(
        name='FakeCourse',
        short_description='ShortDescription',
        description='FullDescription',
        coach=coach1,
        assistant=coach1)
    
    course2 = Course.objects.create(
        name='FakeCourse2',
        short_description='ShortDescription2',
        description='FullDescription2',
        coach=coach1,
        assistant=coach1)
    
    student1 = Student.objects.create(
        name = 'FakeStudent1',
        surname = 'FakeStudentSurname1',
        date_of_birth = '1999-09-09',
        email = 'student1@gmail.com',
        phone = '23123',
        address = 'NY',
        skype = 'skype1')
    student1.courses.add(course1)
    
    student2 = Student.objects.create(
        name = 'FakeStudent2',
        surname = 'FakeStudentSurname2',
        date_of_birth = '1910-02-09',
        email = 'student2@gmail.com',
        phone = '123244',
        address = 'NY',
        skype = 'skype2')
    student2.courses.add(course2)

class StudentsListTest(TestCase):
    def test_student_valid_links(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
    
    def test_student_list_code0(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    
    def test_student_list_number0(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 0) 
    
    def test_student_list_codenot0(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    
    def test_student_list_numbernot0(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)
    
    def test_student_list_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
    
    def test_valid_student_name_edit(self):
        client = Client()
        add_student()
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'FakeStudent1')
        
class StudentsDetailTest(TestCase):
    def test_student_valid_links2(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
    
    def test_detail_name(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'FakeStudent1')  
    
    def test_detail_surname(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'FakeStudentSurname1') 
    
    def test_detail_address(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'NY')
    
    def test_detail_skype(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'skype1') 
    
    def test_student_detail_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
