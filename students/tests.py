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

    def test_students_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/students/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Student registration")

    def test_menu(self):

        from django.test import Client
        client = Client()
        respons = client.get('/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "List of courses")

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

class StudentsDetailTest(TestCase):

    def test_students_detail(self):
        detail = Student.objects.create(
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

    def test_st_delete(self):
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

    def test_st_add(self):

        from django.test import Client
        client = Client()
        respons = client.get('/students/add/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "Student registration")

    def test_st_menu(self):

        from django.test import Client
        client = Client()
        respons = client.get('/')
        self.assertEqual(respons.status_code, 200)
        self.assertContains(respons, "List of courses")

    def test_st_edit(self):
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




