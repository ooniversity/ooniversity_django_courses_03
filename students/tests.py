from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from pybursa.views import IndexView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy


class StudentsListTest(TestCase):

    def test_students_list_all(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student2.courses.add(course2.id)
        
        #print student.courses.get(id=course.id).name
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertContains(response, 'stu')
        self.assertContains(response, 'stu2')


    def test_students_list_all_without_students(self):
        from django.test import Client
        client = Client()
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertEqual(response.status_code, 200)    

    def test_students_list_all_info_surname(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student2.courses.add(course2.id)
        
        #print student.courses.get(id=course.id).name
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertContains(response, 'dent')
        self.assertContains(response, 'dent2')

    def test_students_list_all_info_address(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address2',
            skype='skype')
        student2.courses.add(course2.id)
        
        #print student.courses.get(id=course.id).name
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertContains(response, 'address')
        self.assertContains(response, 'address2')

    def test_students_list_all_info_skype(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address2',
            skype='skype2')
        student2.courses.add(course2.id)
        
        #print student.courses.get(id=course.id).name
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertContains(response, 'skype')
        self.assertContains(response, 'skype2')        
        

    def test_students_list_all_info_courses(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address2',
            skype='skype2')
        student2.courses.add(course2.id)
        
        #print student.courses.get(id=course.id).name
        link = reverse_lazy('students:list_view')
        response = client.get(link)
        self.assertContains(response, 'Course')
        self.assertContains(response, 'Course2')

    def test_students_list_all_in_course(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')

        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        student2 = Student.objects.create(
            name='stu2', surname='dent2', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address2',
            skype='skype2')
        student2.courses.add(course.id)
        student3 = Student.objects.create(
            name='stu3', surname='dent3', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address3',
            skype='skype3')
        student3.courses.add(course2.id)
        
        
        #print student.courses.get(id=course.id).name
        link = '/students/?course_id=%s&page=1' % course.id
        response = client.get(link)
        #print response
        self.assertContains(response, 'stu')
        self.assertContains(response, 'stu2')
        self.assertNotContains(response, 'stu3')

class StudentsDetailTest(TestCase):
    
    def test_detail_response(self):

        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertEqual(response.status_code, 200)

    def test_detail_info_name(self):
        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'stu')

    def test_detail_info_surname(self):
        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'dent')

    

    def test_detail_info_email(self):
        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'first@d.com')

    def test_detail_info_phone(self):
        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, '1234567890')

    def test_detail_info_address(self):
        from django.test import Client
        client = Client()
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'address')

    def test_detail_info_courses(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id)
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'Course')

    def test_detail_info_couple_courses(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(
            name='Course', short_description='short_description', 
            description='description')
        course2 = Course.objects.create(
            name='Course2', short_description='short_description', 
            description='description')
        
        student = Student.objects.create(
            name='stu', surname='dent', date_of_birth='1999-10-10',
            email='first@d.com', phone='1234567890', address='address',
            skype='skype')
        student.courses.add(course.id, course2.id)
        link = reverse_lazy('students:detail', kwargs={'pk': student.id})
        response = client.get(link)
        self.assertContains(response, 'Course')
        self.assertContains(response, 'Course2')        








"""
class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)
"""
