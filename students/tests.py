# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from courses.models import Course
from students.models import Student
import datetime


# Create your tests here.


class Properties(object):
    course_units = 3
    lesson_units = 4
    student_units = 15

    def units_list(self):
        if self.__class__.__name__ is 'CoursesListTest':
            return range(1, self.course_units + 1)
        elif self.__class__.__name__ is 'CoursesDetailTest':
            return range(1, self.lesson_units + 1)
        elif self.__class__.__name__ is 'StudentsListTest':
            return range(1, self.student_units + 1)
        elif self.__class__.__name__ is 'StudentsDetailTest':
            return range(1, self.student_units + 1)

    @classmethod
    def course_add(cls, name='', short_description='', description='', coach=None, assistant=None, ):
        course = Course.objects.create(name=name, short_description=short_description, description=description)

        if coach:
            course.coach.add(coach)

        if assistant:
            course.assistant.add(assistant)

        return course

    @classmethod
    def c_cont_generator(cls, cid=1):
        try:
            cid = str(int(cid))
        except (ValueError, TypeError):
            cid = '1'
        return {
            'name': 'Course test name {0}'.format(cid),
            'short_description': 'Course test short description {0}'.format(cid),
            'description': 'Course test description {0}'.format(cid),
        }

    @classmethod
    def l_cont_generator(cls, lid=1):
        try:
            lid = str(int(lid))
        except (ValueError, TypeError):
            lid = '1'

        return {
            'subject': 'Lesson {0} test subject'.format(lid),
            'description': 'Lesson {0} test description'.format(lid),
            'order': int(lid)
        }

    @classmethod
    def create_student(cls, name, surname, date_of_birth, email, skype, phone, address, courses=None):
        # Create student without courses
        student = Student.objects.create(
            name=name,
            surname=surname,
            date_of_birth=datetime.datetime.strptime(date_of_birth, '%Y-%m-%d').date(),
            email=email,
            skype=skype,
            phone=phone,
            address=address
        )

        # to assign course
        if courses:
            for course in courses:
                student.courses.add(course)

        return student

    @classmethod
    def st_cont_generator(cls, sid=1):
        try:
            sid = str(int(sid))
        except (ValueError, TypeError):
            sid = '1'

        return {
            'name': 'John{0}'.format(sid),
            'surname': 'Doe{0}'.format(sid),
            'date_of_birth': '1961-04-21',
            'email': 'John{0}Doe{0}@example.com'.format(sid),
            'phone': '+38050123{ending}'.format(ending='{0:04d}'.format(int(sid))),
            'address': 'ul. Astronomicheskaya {0}, kv. {0}, Kharkov, 12345, UKRAINE'.format(sid),
            'skype': 'John{0}Doe{0}'.format(sid),
        }


class StudentsListTest(TestCase, Properties):
    def test_reachability(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)
        return response

    def test_data_insert(self):

        courses = dict()
        # insert test_data
        for i in self.units_list():
            self.c_cont_generator(i)
            courses[i] = self.course_add(**self.c_cont_generator(i))

        pushed_data = dict()
        for i in self.units_list():
            if i % 3 == 0:
                st_courses = [courses[3], courses[2], courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            elif i % 2 == 0:
                st_courses = [courses[3], courses[2]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            else:
                st_courses = [courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))

        # counted elem validation
        response = self.test_reachability()
        return {'pushed_data': pushed_data, 'response': response}

    def test_mandatory_content(self):
        url = reverse('students:list_view')
        # insert test_data
        courses = dict()
        # insert test_data
        for i in self.units_list():
            self.c_cont_generator(i)
            courses[i] = self.course_add(**self.c_cont_generator(i))

        pushed_data = dict()
        for i in self.units_list():
            if i % 3 == 0:
                st_courses = [courses[3], courses[2], courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            elif i % 2 == 0:
                st_courses = [courses[3], courses[2]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            else:
                st_courses = [courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))

        response = self.client.get(url)

        self.assertContains(response, '<!-- notification area -->')

        # add main button validation:
        self.assertContains(response, reverse('students:add'))

        # table & links validation
        for pk in range(1, 3):
            self.assertContains(response, pk)
            self.assertContains(response, pushed_data[pk].name)
            self.assertContains(response, pushed_data[pk].surname)

            self.assertContains(response, '{}{}'.format(url, pk))

            # edit & del buttons validation:
            self.assertContains(response, reverse('students:edit', args=(pk,)))
            self.assertContains(response, reverse('students:remove', args=(pk,)))

    def test_add_form_blank(self):
        # insert test_unit_data
        response = self.client.get(reverse('students:add'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="surname"')
        self.assertContains(response, 'name="date_of_birth"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="phone"')
        self.assertContains(response, 'name="address"')
        self.assertContains(response, 'name="skype"')
        self.assertContains(response, 'name="courses"')

        # fails blanks test
        response = self.client.post(reverse('courses:add'), {})  # blank data dictionary
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'short_description', 'This field is required.')
        self.assertFormError(response, 'form', 'description', 'This field is required.')

    def test_add_form_post(self):
        # insert test_unit_data
        self.test_data_insert()

        response = self.client.get(reverse('students:add'))
        self.assertEqual(response.status_code, 200)

        content = self.st_cont_generator(self.student_units + 2)
        content['courses'] = '1'
        response = self.client.post(reverse('students:add'), content, follow=True)
        self.assertRedirects(response, reverse('students:list_view'))


class StudentsDetailTest(TestCase, Properties):
    def test_data_insert(self):
        courses = dict()
        # insert test_data
        for i in self.units_list():
            self.c_cont_generator(i)
            courses[i] = self.course_add(**self.c_cont_generator(i))

        pushed_data = dict()
        for i in self.units_list():
            if i % 3 == 0:
                st_courses = [courses[3], courses[2], courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            elif i % 2 == 0:
                st_courses = [courses[3], courses[2]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))
            else:
                st_courses = [courses[1]]
                pushed_data[i] = self.create_student(courses=st_courses, **self.st_cont_generator(i))

        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)

        return {'pushed_data': pushed_data, 'response': response}

    def test_reachability(self):
        pushed_data = self.test_data_insert()['pushed_data']
        response = self.client.get(reverse('students:detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

        return {'pushed_data': pushed_data, 'response': response}

    def test_del_form(self):
        # insert test_unit_data
        self.test_data_insert()

        response = self.client.get(reverse('students:remove', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_del_redirect(self):
        # insert test_unit_data
        self.test_del_form()

        response = self.client.post(reverse('students:remove', args=(1,)), {}, follow=True)
        self.assertRedirects(response, reverse('students:list_view'))

    def test_edit_form(self):
        # insert test_unit_data
        self.test_data_insert()

        response = self.client.get(reverse('students:edit', args=(1,)))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('students:edit', args=(1,)), {'name': 'Test_name'}, follow=True)
        self.assertEqual(response.status_code, 200)
