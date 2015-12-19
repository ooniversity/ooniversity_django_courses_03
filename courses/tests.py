# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from courses.models import Course, Lesson


# Create your tests here.


class Properties(object):
    course_units = 3
    lesson_units = 4

    def units_list(self):
        if self.__class__.__name__ is 'CoursesListTest':
            return range(1, self.course_units + 1)
        elif self.__class__.__name__ is 'CoursesDetailTest':
            return range(1, self.lesson_units + 1)

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


class CoursesListTest(TestCase, Properties):
    def test_reachability(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        return response

    def test_data_insert(self):
        pushed_data = dict()
        # insert test_data
        for i in self.units_list():
            pushed_data[i] = self.c_cont_generator(i)
            self.course_add(**self.c_cont_generator(i))

        # counted elem validation
        response = self.test_reachability()
        self.assertEqual(Course.objects.all().count(), self.course_units)
        return {'pushed_data': pushed_data, 'response': response}

    def test_mandatory_content(self):
        # insert test_data
        response = self.test_data_insert()
        pushed_data = response['pushed_data']
        response = response['response']

        self.assertContains(response, '<!-- notification area -->')

        # add main button validation:
        self.assertContains(response, reverse('courses:add'))

        # table & links validation
        for pk in self.units_list():
            self.assertContains(response, reverse('courses:detail', args=(pk,)))
            self.assertContains(response, str(pk).upper())
            self.assertContains(response, pushed_data[pk]['name'].upper())
            self.assertContains(response, pushed_data[pk]['short_description'].title())
            # edit & del buttons validation:
            self.assertContains(response, reverse('courses:edit', args=(pk,)))
            self.assertContains(response, reverse('courses:remove', args=(pk,)))

    def test_add_form_blank(self):
        # insert test_unit_data
        response = self.client.get(reverse('courses:add'))
        self.assertEqual(response.status_code, 200)

        form_fields_all = ['name', 'short_description', 'description', 'coach', 'assistant', ]
        for field in form_fields_all:
            self.assertContains(response, 'name="{}"'.format(field))

        # fails blanks test
        response = self.client.post(reverse('courses:add'), {})  # blank data dictionary
        required_fields = ['name', 'short_description', 'description', ]
        for field in required_fields:
            self.assertFormError(response, 'form', '{}'.format(field), 'This field is required.')

    def test_add_form_post(self):
        # insert test_unit_data
        response = self.client.get(reverse('courses:add'))
        self.assertEqual(response.status_code, 200)

        content = self.c_cont_generator(self.course_units + 2)
        response = self.client.post(reverse('courses:add'), content, follow=True)
        self.assertRedirects(response, reverse('index'))


class CoursesDetailTest(TestCase, Properties):
    def test_data_insert(self):
        test_course = self.course_add(**self.c_cont_generator())
        pushed_data = dict()
        for i in self.units_list():
            pushed_data[i] = self.l_cont_generator(lid=i)
            Lesson.objects.create(course=test_course, **pushed_data[i])
            pushed_data[i]['course_name'] = test_course.name

        # counted elem validation
        self.assertEqual(Lesson.objects.all().count(), self.lesson_units)

        return {'pushed_data': pushed_data, 'test_course': test_course}

    def test_reachability(self, pk=1):
        pushed_data = self.test_data_insert()['pushed_data']
        response = self.client.get(reverse('courses:detail', args=(pk,)))
        self.assertEqual(response.status_code, 200)

        return {'pushed_data': pushed_data, 'response': response}

    def test_mandatory_content(self):
        cid = 1
        response = self.test_reachability(cid)
        pushed_data = response['pushed_data']
        response = response['response']

        self.assertContains(response, '<!-- notification area -->')

        # add main button validation:
        self.assertContains(response, reverse('courses:add-lesson', args=(cid,)))

        for pk in self.units_list():
            self.assertContains(response, pushed_data[pk]['order'])
            self.assertContains(response, pushed_data[pk]['subject'])
            self.assertContains(response, pushed_data[pk]['description'])

    def test_add_form_blank(self):
        # insert test_unit_data
        response = self.client.get(reverse('courses:add-lesson', args=(1,)))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'name="subject"')
        self.assertContains(response, 'name="description"')
        self.assertContains(response, 'name="course"')
        self.assertContains(response, 'name="order"')

        # fails blanks test
        response = self.client.post(reverse('courses:add-lesson', args=(1,)), {})  # blank data dictionary
        self.assertFormError(response, 'form', 'subject', 'This field is required.')
        self.assertFormError(response, 'form', 'description', 'This field is required.')
        self.assertFormError(response, 'form', 'order', 'This field is required.')

    def test_add_form_post(self):
        data = self.test_data_insert()
        response = self.client.get(reverse('courses:detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('courses:add-lesson', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)

        content = self.l_cont_generator(self.lesson_units + 2)
        # content['course'] = test_course.id
        content['course'] = data['test_course'].id
        response = self.client.post(reverse('courses:add-lesson', args=(1,)), content, follow=True)
        self.assertRedirects(response, reverse('courses:detail', args=(1,)))
