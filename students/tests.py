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

    def test_students_detail(self):
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


class StudentsAddTest(TestCase):

    def test_students_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/students/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Student registration")


class StudentsEditTest(TestCase):

    def test_students_edit(self):
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
        respons = client.get('/students/edit/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Student info update")


class StudentsDeleteTest(TestCase):

    def test_students_delete(self):
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
        respons = client.get('/students/remove/1/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Student info suppression")





