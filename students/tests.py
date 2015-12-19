# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from models import Student
from courses.models import Course
from courses.tests import create_courses


def create_students():
    items = {}
    courses = create_courses()
    for i in courses:
        for id in range(1,4):
            items['student_' + i + str(id)] = Student.objects.create(
            name = 'student%d' % id,
            surname = '%dstudent' %id,
            date_of_birth = '2015-01-0%d' % id,
            email = 'student_%d@email.com' % id,
            phone = str(id) * 10,
            address = 'student %d address' % id,
            skype = 'student.skype %d' % id 
            )
            items['student_' + i + str(id)].courses.add(courses[i].id)
    return items



class StudentsDetailTest(TestCase):

    def test_student_detail_not_found(self):
        client = Client()
        response = client.get('/students/1/')  
        self.assertEqual(response.status_code, 404)
    
    def test_student_detail_normal_response(self):
        client = Client()
        items = create_students()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_detail_have_title(self):
        client = Client()
        items = create_students()
        for i in items:
            response = client.get('/students/%d/' % items[i].id)
            self.assertContains(response, '<title>Pybursa Students %s %s info</title>' % (items[i].name, items[i].surname))

    def test_student_detail_header(self):
        client = Client()
        items = create_students()       
        for i in items:
            response = client.get('/students/%d/' % items[i].id)  
            self.assertContains(response, '<h2 class="sub-header">%s %s</h2>' % ( items[i].name, items[i].surname ))

    def test_student_detail_email(self):
        client = Client()
        items = create_students()       
        for i in items:
            response = client.get('/students/%d/' % items[i].id)  
            self.assertContains(response, '<td>%s</td>' % items[i].email)
            

    
class StudentsListTest(TestCase):

    def test_student_add_button(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, '<a href="/students/add/')

    def test_student_lists_normal_response(self):
        client = Client()
        response = client.get('/students/?course_id=1')  
        self.assertEqual(response.status_code, 200)

    def test_student_lists_course_pages(self):
        client = Client()
        response = client.get('/students/?course_id=1') 
        items = create_students()
        for n in items:
            for i in items[n].courses.all():
                students_count = len(Student.objects.filter(courses=i.id))
                if students_count % 2 == 0:
                    pages = students_count / 2
                else:
                    pages = students_count / 2 + 1
                response = client.get('/students/?course_id=%d&page=1' % 1 )  
                self.assertEqual(response.status_code, 200)

    def test_student_lists_pages(self):
        client = Client()
        response = client.get('/students/?course_id=1') 
        items = create_students()
        for i in items:
            if items[i].id % 2 == 0:
                page = items[i].id / 2
            else:
                page = items[i].id / 2 + 1
            response = client.get('/students/?page=%d' % page )  
            self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_list_title(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Pybursa Students')



