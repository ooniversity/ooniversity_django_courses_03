# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from models import Course, Lesson
from courses.views import add_lesson

def create_courses():
        some_courses = {}
        some_courses['course1'] = Course.objects.create(
                                name ='Pybursa02',
                                short_description="Some short description",
                                description = "Some long description")
        some_courses['course2'] = Course.objects.create(
                                name ='Pybursa03',
                                short_description="Some short description",
                                description = "Some long description")
        for course in some_courses:
            lesson = Lesson.objects.create(
                                    subject = 'Some Web topic',
                                    description = 'Good description for our subject',
                                    course = Course.objects.get(id=some_courses[course].id),
                                    order = 1)
        return some_courses

class CoursesListTest(TestCase):

    def test_course_create(self):
        client = Client()
        course1 = create_courses()
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_page_have_title(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Pybursa Main')


    def test_course_list_page_have_courses(self):
        client = Client()
        course1 = create_courses()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class CoursesDetailTest(TestCase):

    def test_course_detail_page_have_title(self):
        client = Client()
        course = create_courses()
        for i in course:
            response = client.get('/courses/%d/' % course[i].id)
            self.assertContains(response, '<title>%s Description</title>' % course[i].name )

    def test_course_list_links(self):
        response = self.client.get('/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')

    def test_course_page_no_courses(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_page_have_courses(self):
        client = Client()
        course1 = create_courses()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_page_have_course_description(self):
        client = Client()
        course = create_courses()
        for i in course:
            response = client.get('/courses/%d/' % course[i].id)
            self.assertContains(response, '<h2>%s</h2>' % course[i].description )

