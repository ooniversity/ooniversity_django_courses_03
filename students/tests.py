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


class StudentsListTest(TestCase):
    courses_number = 3
    students_number = random.randrange(1, 4)

    courses = CoursesListTest()
    courses_list = courses.courses_generator(courses_number)

    def runTest(self):
        pass

    def students_create(self):
        rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
        rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
        short_description = "This is the test short_description"
        description = "This is the test full description"

        user = User.objects.create(username='test_user_' + rnd_s)
        coach = Coach.objects.create(user=user,
                                     date_of_birth=date.today(),
                                     phone=rnd_n,
                                     address='This is the test address for ' + rnd_s,
                                     skype=rnd_s + '_skype',
                                     )
        assistant = self.coach_create(rnd_s + '_a')

        for i in range(self.courses_number):
            course = Course.objects.create(name='course_' + random_name,
                                           short_description=short_description,
                                           description=description,
                                           coach=coach,
                                           assistant=assistant,
                                           )

            student = Student.objects.create(name='test_student_' + rnd_s,
                                             surname=rnd_n,
                                             date_of_birth=date.today(),
                                             email=rnd_s + '@test.st',
                                             phone=rnd_n,
                                             address='This is the test address for ' + rnd_s,
                                             skype=rnd_s + '_skype',
                                             )
            student.courses.add(course)



        # for course in self.courses_list:
        #     for s_i in xrange(self.students_number):
        #         rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
        #         rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
        #
        #         student = Student.objects.create(name='test_student_' + rnd_s,
        #                                          surname=rnd_n,
        #                                          date_of_birth=date.today(),
        #                                          email=rnd_s + '@test.st',
        #                                          phone=rnd_n,
        #                                          address='This is the test address for ' + rnd_s,
        #                                          skype=rnd_s + '_skype',
        #                                          )
        #         import pdb; pdb.set_trace()
        #         student.courses.add(course)
        #         students_list.append(student)



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


# class StudentsDetailTest(TestCase):
#
#     students = StudentsListTest()
#
#     def test_student_details_template(self):
#
#         self.students.students_create()
#
#         client = Client()
#         response = client.get('/students/1/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response.content, 'students/student_detail.html')
#
#     def test_student_name_in_header(self):
#         students = self.students.students_create()
#         client = Client()
#         for i in range(len(students)):
#             student = students[i]
#             s_id = student.id
#             s_name = student.name
#             response = client.get('/students/%d/' % s_id)
#             # import pdb; pdb.set_trace()
#             self.assertEqual(response.status_code, 200)
#             self.assertRegexpMatches(str(response), r'<h[123]>%s</h[123]>' % s_name)
