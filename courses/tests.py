# -*- coding:UTF-8 -*-

import random, string
from datetime import date
from django.test import TestCase, Client
from django.contrib.auth.models import User
from coaches.models import Coach
from courses.models import Course
from django.core.urlresolvers import reverse


# class CreateCoursesForTest(object):
#
#     def __init__(self, courses_number=None):
#         if courses_number is None:
#             self.courses_number = 1


class CoursesListTest(TestCase):

    courses_number = 3

    def user_create(self, name):
        """ https://docs.djangoproject.com/en/1.7/ref/contrib/auth/#user """
        prefix = 'test_user_'
        username = prefix + name
        email = prefix + name + "@test.ua"
        first_name = prefix + "first_name"
        last_name = prefix + "last_name"
        password = prefix + "password"
        user = User.objects.create_user(username=username,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name,
                                        password=password,
                                        )
        return user

    def coach_create(self, name):
        prefix = 'test_coach_'
        name = prefix + name
        date_of_birth = date.today()
        gender = random.choice('MF')
        phone = "".join([random.choice(string.digits) for i in xrange(11)])
        address = "This is the test address"
        skype = prefix + "skype"
        description = "This is the test description"
        coach = Coach.objects.create(user=self.user_create(name),
                                     date_of_birth=date_of_birth,
                                     gender=gender,
                                     phone=phone,
                                     address=address,
                                     skype=skype,
                                     description=description,
                                     )
        return coach

    def courses_generator(self, courses_number):

        courses_list = []

        short_description = "This is the test short_description"
        description = "This is the test full description"

        for i in range(courses_number):

            random_name = "".join([random.choice(string.letters) for i in xrange(5)])

            coach = self.coach_create(random_name)

            assistant = self.coach_create(random_name + '_a')

            course = Course.objects.create(name='course_' + random_name,
                                           short_description=short_description,
                                           description=description,
                                           coach=coach,
                                           assistant=assistant,
                                           )

            courses_list.append(course)

        return courses_list

    def test_getting_index_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_button_main_and_active(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '<li class="active"><a href="/">Главная</a></li>')

    def test_courses_presence_on_page(self):

        self.courses_generator(self.courses_number)

        client = Client()
        response = client.get('/')
        context_c = response.context['courses']
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context_c), self.courses_number)

    def test_check_course_edit_button_equality(self):

        self.courses_generator(self.courses_number)

        client = Client()
        response = client.get('/')
        content = response.content
        real_buttons_number = content.count('<a href="/courses/edit/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, self.courses_number)

    def test_check_course_remove_button_equality(self):

        self.courses_generator(self.courses_number)

        client = Client()
        response = client.get('/')
        content = response.content
        real_buttons_number = content.count('<a href="/courses/remove/')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(real_buttons_number, self.courses_number)


class CoursesDetailTest(CoursesListTest):

    def test_resolve_course_details(self):
        self.courses_generator(self.courses_number)
        client = Client()
        for i in range(1, 4):
            response = client.get('/courses/%d/' % i)
            self.assertEqual(response.status_code, 200)

    def test_presence_of_add_lesson_link(self):
        courses = self.courses_generator(self.courses_number)
        client = Client()
        for i in range(len(courses)+1):
            course = courses[i]
            cid = course.id
            response = client.get('/courses/%d/' % cid)
            self.assertEqual(response.status_code, 200)
            # self.assertContains(response, '<a href="/courses/%d/add_lesson">Добавить занятие</a>' % i)
            self.assertRegexpMatches(str(response), r'<a.*href=\'?\"?/courses/%d/add_lesson\'?\"?>.*</a>' % cid)

#  <h1>one plus x</h1>