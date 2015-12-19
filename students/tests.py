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

    def test_simple(self):
        CoursesListTest.test_courses_presence_on_page(self.courses)
        import pdb; pdb.set_trace()




'''
    def students_create(self):
        for i in xrange(self.courses_number):
            instance = CoursesListTest()
            for j in xrange(self.students_number):
                rnd_c = "".join([random.choice(string.letters) for i in xrange(5)])
                rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
                student = Student.objects.create(name='test_student',
                                                 surname=rnd_c,
                                                 date_of_birth=date.today(),
                                                 email=rnd_c + '@test.st',
                                                 phone=rnd_n,
                                                 address='This is the test address for ' + rnd_c,
                                                 skype=rnd_c + '_skype',
                                                 )
                student.courses.add(CoursesListTest.courses_generator(instance, 1))

    def test_students_presence_on_page(self):

        self.students_create()

        client = Client()
        response = client.get('/students/')
        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)

'''
