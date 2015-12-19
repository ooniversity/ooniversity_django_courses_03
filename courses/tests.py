# -*- coding:UTF-8 -*-

import random, string
from datetime import date
from django.test import TestCase, Client
from django.contrib.auth.models import User
from coaches.models import Coach
from courses.models import Course
from django.core.urlresolvers import reverse


class CoursesListTest(TestCase):
    courses_number = 5

    def user_create(self, name):
        """ https://docs.djangoproject.com/en/1.7/ref/contrib/auth/#user """
        prefix = 'test_user_'
        username = prefix + name
        email = prefix + name + "@test.ua"
        first_name = prefix + "first_name"
        last_name = prefix + "last_name"
        password = prefix + "password"
        return User.objects.create_user(username=username,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name,
                                        password=password,
                                        )

    def coach_create(self, coach):
        prefix = 'test_coach_'
        date_of_birth = date.today()
        gender = random.choice('MF')
        phone = "".join([random.choice(string.digits) for i in xrange(11)])
        address = "This is the test address"
        skype = prefix + "skype"
        description = "This is the test description"
        return Coach.objects.create(user=self.user_create(coach),
                                    date_of_birth=date_of_birth,
                                    gender=gender,
                                    phone=phone,
                                    address=address,
                                    skype=skype,
                                    description=description,
                                    )

    def course_create(self, course):
        name = course
        short_description = "This is the test short_description"
        description = "This is the test full description"
        coach = self.coach_create("".join([random.choice(string.letters) for i in xrange(5)]))
        assistant = self.coach_create("".join([random.choice(string.letters) for i in xrange(5)]))

        return Course.objects.create(name=name,
                                     short_description=short_description,
                                     description=description,
                                     coach=coach,
                                     assistant=assistant,
                                     )

    def courses_generator(self, number):
        courses_number = number

        for i in range(courses_number):
            course_name = ("test_course_" + "".join([random.choice(string.letters) for i in xrange(5)]))
            self.course_create(course_name)

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


class CoursesDetailTest(TestCase):

    def test_resolve_course_details(self):

        client = Client()

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_presence_of_add_lesson_button(self):

        client = Client()
        response = client.get('/courses/1/')
        content = response.content
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/add_lesson')
