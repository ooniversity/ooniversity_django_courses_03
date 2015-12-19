from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse
import datetime

def create_course(name):
    return Course.objects.create(
        name=name,
        short_description='CourseShortDescription',
        description='CourseFullDescription')  

class StudentsListTest(TestCase):
    def test_students_list(self): 
        from django.test import Client
        client = Client()

        student1 = Student.objects.create(
            name='FakeStudentName1', 
            surname='FakeStudentSurname1',
            date_of_birth='1900-12-01',
            email='email1@gmail.com',
            phone='02020202020',
            address='address1',
            skype='skype1')

        student2 = Student.objects.create(
            name='FakeStudentName2', 
            surname='FakeStudentSurname2',
            date_of_birth="1891-01-30",
            email='email2@gmail.com',
            phone='0291094893',
            address='address2',
            skype='skype2')

        course1 = create_course('CourseName1')
        student1.courses.add(course1)
        student2.courses.add(course1)

        response = client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Student.objects.all().count(), 2)
 
        self.assertTrue('student_list' in response.context)

        for student in Student.objects.all():
            self.assertContains(response, student.name)

        for student in Student.objects.all():
            self.assertContains(response, student.address)

        for student in Student.objects.all():
            self.assertContains(response, student.skype)

        self.assertEqual(response.context['student_list'][0], 
                         student1) 
        self.assertEqual(response.context['student_list'][1], 
                         student2) 

        self.assertEqual(student1.email, 'email1@gmail.com')
        self.assertEqual(student2.email, 'email2@gmail.com')

        self.assertContains(response, 'CourseName1')
        self.assertEqual(response.context['student_list'][0].courses.all()[0].name, course1.name) 
        self.assertEqual(response.context['student_list'][1].courses.all()[0].name, course1.name) 
       

class StudentsDetailTest(TestCase):
    def test_student_detail(self):
        from django.test import Client
        client = Client()

        response = client.get(reverse(
                                'students:detail', 
                                args=(1,)))
        self.assertEqual(response.status_code, 404) 

        student1 = Student.objects.create(
            name='FakeStudentName1', 
            surname='FakeStudentSurname1',
            date_of_birth='1891-01-30',
            email='email1@email.email',
            phone='02030100',
            address='address1',
            skype='skype1')

        course1 = create_course('CourseName1')
        course2 = create_course('CourseName2')
        student1.courses.add(course1)
        student1.courses.add(course2)
        response = client.get(reverse(
                                 'students:detail', 
                                 args=(student1.pk,)))
        self.assertEqual(response.status_code, 200)    
        self.assertTrue('student' in response.context) 
        self.assertContains(response, "FakeStudentName1")  
        self.assertEqual(response.context['student'].pk, student1.pk)   
        self.assertEqual(response.context['student'].name, 
                         'FakeStudentName1')
        self.assertEqual(response.context['student'].surname,
                         student1.surname) 
        self.assertContains(response, student1.name)
        self.assertContains(response, student1.surname)
        self.assertContains(response, student1.email)
        self.assertContains(response, student1.phone)
        self.assertContains(response, student1.address)
        self.assertContains(response, student1.skype)

        self.assertEqual(response.context['student'].email, 
                         student1.email) 
        self.assertEqual(response.context['student'].phone,
                         student1.phone) 
        self.assertEqual(response.context['student'].address,
                         student1.address)  
        self.assertEqual(response.context['student'].skype, 
                         student1.skype)   

        self.assertContains(response, 'CourseName1')
        self.assertContains(response, 'CourseName2')
        self.assertEqual(response.context['student'].courses.all()[0].name, course1.name) 
        self.assertEqual(response.context['student'].courses.all()[1].name, course2.name) 
        courses = student1.courses.all()
        self.assertEqual(courses.count(), 2)
        self.assertEqual(courses[0].pk, course1.pk)
        self.assertEqual(courses[1].pk, course2.pk)