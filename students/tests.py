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

    courses = CoursesListTest()
    courses_list = courses.courses_generator(courses_number)

    def students_create(self):

        for course in self.courses_list:
            for s_i in xrange(self.students_number):
                rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
                rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])

                student = Student.objects.create(name='test_student_' + rnd_s,
                                                 surname=rnd_n,
                                                 date_of_birth=date.today(),
                                                 email=rnd_s + '@test.st',
                                                 phone=rnd_n,
                                                 address='This is the test address for ' + rnd_s,
                                                 skype=rnd_s + '_skype',
                                                 )
                student.courses.add(course)

    def test_response_status(self):

        self.students_create()

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

        self.students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/edit/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 2)

    def test_check_student_remove_button_equality(self):

        self.students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/remove/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 2)

    def test_pagination(self):

        self.students_create()

        client = Client()
        response = client.get('/students/?page=2')
        self.assertEqual(response.status_code, 200)


class StudentsDetailTest(TestCase):

    def test_student_details_template(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response.content, 'students/student_detail.html')
