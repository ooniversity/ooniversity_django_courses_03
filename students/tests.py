# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student

class StudentsListTest(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_students_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_page_fails(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)


