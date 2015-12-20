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


def create_course(name):
    return Course.objects.create(
        name=name,
        short_description="This is the test short_description",
        description="This is the test full description")


class StudentTests(TestCase):
    def test_students_list(self):

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

        course_n = create_course('course_' + rnd_s)
        student_n.courses.add(course_n)
        client = Client()
        response = client.get(reverse('students:students'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)


# def course_create():
#     test_user = User.objects.create(username='test')
#     test_coach = Coach.objects.create(user=test_user,
#                                       date_of_birth=date.today(),
#                                       phone='888888',
#                                       address='qqqq',
#                                       skype='wwww',
#                                       description='rrrr')
#     course = Course.objects.create(name='yyyyy',
#                                    short_description='yyyyyyyyyyy',
#                                    description='ddddddddddyyg',
#                                    coach=test_coach,
#                                    assistant=test_coach)
#     return course
#
#
# def students_create():
#     course = course_create()
#     student = Student.objects.create(name='111111111111',
#                                      surname='2222222222222222222',
#                                      date_of_birth=date.today(),
#                                      email='1111111@222222222.333',
#                                      phone='444444444444444',
#                                      address='555555555555555555',
#                                      skype='6666666666666666666',
#                                      )
#     student.courses.add(course)
#     return student
#
# # def students_create():
# #
# #     imp = CoursesListTest()
# #
# #     rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
# #     rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
# #
# #     student = Student.objects.create(name='test_student_' + rnd_s,
# #                                      surname=rnd_n,
# #                                      date_of_birth=date.today(),
# #                                      email=rnd_s + '@test.st',
# #                                      phone=rnd_n,
# #                                      address='This is the test address for ' + rnd_s,
# #                                      skype=rnd_s + '_skype',
# #                                      courses=[4],
# #                                      )
#
#     # import pdb; pdb.set_trace()
#     # course_id = imp.courses_generator(1)[0].id
#     #student.courses.add(5)
#
#
# class StudentsListTest(TestCase):
#     # courses_number = 3
#     # students_number = random.randrange(1, 4)
#     #
#     # courses = CoursesListTest()
#     # courses_list = courses.courses_generator(courses_number)
#
#     def runTest(self):
#         pass
#
#     # def students_create(self):
#     #     rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
#     #     rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
#     #     short_description = "This is the test short_description"
#     #     description = "This is the test full description"
#     #
#     #     user_c = User.objects.create(username='test_user_' + rnd_s)
#     #     user_a = User.objects.create(username='test_user_' + rnd_s + '_a')
#     #     coach = Coach.objects.create(user=user_c,
#     #                                  date_of_birth=date.today(),
#     #                                  phone=rnd_n,
#     #                                  address='This is the test address for ' + rnd_s,
#     #                                  skype=rnd_s + '_skype',
#     #                                  )
#     #     assistant = Coach.objects.create(user=user_a,
#     #                                      date_of_birth=date.today(),
#     #                                      phone=rnd_n,
#     #                                      address='This is the test address for ' + rnd_s,
#     #                                      skype=rnd_s + '_skype',
#     #                                      )
#     #
#     #     course = Course.objects.create(name='course_' + rnd_s,
#     #                                    short_description=short_description,
#     #                                    description=description,
#     #                                    coach=coach,
#     #                                    assistant=assistant,
#     #                                    )
#
#
#
#         # for course in self.courses_list:
#         #     for s_i in xrange(self.students_number):
#         #         rnd_s = "".join([random.choice(string.letters) for i in xrange(5)])
#         #         rnd_n = "".join([random.choice(string.digits) for i in xrange(11)])
#         #
#         #         student = Student.objects.create(name='test_student_' + rnd_s,
#         #                                          surname=rnd_n,
#         #                                          date_of_birth=date.today(),
#         #                                          email=rnd_s + '@test.st',
#         #                                          phone=rnd_n,
#         #                                          address='This is the test address for ' + rnd_s,
#         #                                          skype=rnd_s + '_skype',
#         #                                          )
#         #         import pdb; pdb.set_trace()
#         #         student.courses.add(course)
#         #         students_list.append(student)
#


    def test_response_status(self):

        student = students_create()

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


class StudentsDetailTest(TestCase):

    students = StudentsListTest()

    def test_student_details_template(self):

        # students = self.students

        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response.content, 'students/student_detail.html')

    def test_student_name_in_header(self):
        # students = self.students
        client = Client()
        for i in range(len(self.students)):
            student = students[i]
            s_id = student.id
            s_name = student.name
            response = client.get('/students/%d/' % s_id)
            import pdb; pdb.set_trace()
            self.assertEqual(response.status_code, 200)
            self.assertRegexpMatches(str(response), r'<h[123]>%s</h[123]>' % s_name)
