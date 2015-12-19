# -*- coding:UTF-8 -*-

import random, string
from datetime import date
from django.test import TestCase, Client
from courses.tests import CoursesListTest
from django.contrib.auth.models import User
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse


class StudentsListTest(TestCase):
    courses_number = 3
    students_number = random.randrange(1, 4)

    def course_students_create(self):

        rnd_c = "".join([random.choice(string.letters) for i in xrange(5)])

        for c_i in range(self.courses_number):
            course_name = ("test_course_" + rnd_c)
            short_description = "This is the test short_description for " + rnd_c
            description = "This is the test full description for " + rnd_c

            course = Course.objects.create(name=course_name,
                                           short_description=short_description,
                                           description=description,
                                           )
            for s_i in xrange(self.students_number):
                rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
                rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])

                student = Student.objects.create(name='test_student',
                                                 surname=rnd_s,
                                                 date_of_birth=date.today(),
                                                 email=rnd_s + '@test.st',
                                                 phone=rnd_n,
                                                 address='This is the test address for ' + rnd_s,
                                                 skype=rnd_s + '_skype',
                                                 )
                student.courses.add(course)

    def test_response_status(self):

        self.course_students_create()

        client = Client()
        response = client.get('/students/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_student_list_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response.content, 'students/student_list.html')

    def test_check_student_edit_button_equality(self):

        self.course_students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/edit/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 2)

    def test_check_student_remove_button_equality(self):

        self.course_students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/remove/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 2)

    def test_pagination(self):
        client = Client()
        response = client.get('/students/?page=1')
        self.assertEqual(response.status_code, 200)


class StudentsDetailTest(TestCase):
    def test_resolve_student_details3(self):
        client = Client()

        response = client.get('/student/1/')
        self.assertEqual(response.status_code, 404)

    def test_resolve_student_details4(self):
        client = Client()

        response = client.get('/student/9/')
        self.assertEqual(response.status_code, 404)

    def test_resolve_student_details6(self):
        client = Client()

        response = client.get('/student/6/')
        self.assertEqual(response.status_code, 404)

    def test_resolve_student_details7(self):
        client = Client()

        response = client.get('/student/5/')
        self.assertEqual(response.status_code, 404)

    def test_resolve_student_details8(self):
        client = Client()

        response = client.get('/student/4/')
        self.assertEqual(response.status_code, 404)

    def test_resolve_student_detai8(self):
        client = Client()

        response = client.get('/student/3/')
        self.assertEqual(response.status_code, 404)


'''
    def test_ability_to_add_student(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, '<a href="/students/add/')
'''
