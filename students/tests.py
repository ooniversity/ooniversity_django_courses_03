from django.test import TestCase
from students.models import Student


class StudentsListTest(TestCase):

    def test_students_list(self):
        student = Student.objects.create(
            name = 'Petya',
            surname = 'Sidorov',
            date_of_birth = '2010-01-01',
            email = 'email@gmail.com',
            phone = '11111',
            address = 'address',
            skype = 'skype',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/students/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Petya")


class StudentsDetailTest(TestCase):

    def test_students_list(self):
        student = Student.objects.create(
            name = 'Petya',
            surname = 'Sidorov',
            date_of_birth = '2010-01-01',
            email = 'email@gmail.com',
            phone = '11111',
            address = 'address',
            skype = 'skype',
        )

        from django.test import Client
        client = Client()
        respons = client.get('/students/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Petya")


