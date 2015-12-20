# -*- coding:UTF-8 -*-

import random, string
from datetime import date
from django.test import TestCase, Client
from courses.tests import CoursesListTest
from django.contrib.auth.models import User
from students.models import Student
from coaches.models import Coach
from courses.models import Course
from django.core.urlresolvers import reverse


class CreateAll(object):

    def create_course(name):
        return Course.objects.create(
            name=name,
            short_description="This is the test short_description",
            description="This is the test full description")

    def create_students_list(self):

        rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
        rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])

        student_n = Student.objects.create(name='test_student_' + rnd_s,
                                           surname=rnd_n,
                                           date_of_birth=date.today(),
                                           email=rnd_s + '@test.st',
                                           phone=rnd_n,
                                           address='This is the test address for ' + rnd_s,
                                           skype=rnd_s + '_skype',
                                           )

        course_n = self.create_course('course_' + self.rnd_s)

        return student_n.courses.add(course_n)


class StudentTests(TestCase):

    def test_student_list(self):
        client = Client()
        student = CreateAll()
        student.create_students_list()
        response = client.get(reverse('students:list_view'))
        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)

    def test_response_status(self):

        # student = students_create()

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

        # students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/edit/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 1)

    def test_check_student_remove_button_equality(self):
        #
        # students_create()

        client = Client()
        response = client.get('/students/')
        content = response.content
        real_buttons_number = content.count('<a href="/students/remove/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, 1)

    def test_pagination(self):

        # students_create()

        client = Client()
        response = client.get('/students/?page=1')
        self.assertEqual(response.status_code, 200)


# class StudentsDetailTest(TestCase):
#
#     # students = StudentsListTest()
#
#     def test_student_details_template(self):
#
#         # students = self.students
#
#         client = Client()
#         response = client.get('/students/1/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response.content, 'students/student_detail.html')
#
#     def test_student_name_in_header(self):
#         # students = self.students
#         client = Client()
#         for i in range(len(self.students)):
#             student = students[i]
#             s_id = student.id
#             s_name = student.name
#             response = client.get('/students/%d/' % s_id)
#             import pdb; pdb.set_trace()
#             self.assertEqual(response.status_code, 200)
#             self.assertRegexpMatches(str(response), r'<h[123]>%s</h[123]>' % s_name)
