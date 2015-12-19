from django.test import TestCase
from students.models import Student


# Create your tests here.
class StudentsListTest(TestCase):
    def test_page_students_list(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ksenia_Test Kolomiets_Test")

    def test_page_students_list_empty(self):
        from django.test import Client
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No students are available.")

    def test_add_new_student_link_presence(self):
        from django.test import Client
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add a new student")

    def test_students_list_next_page_link_presence(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29')
        student2 = Student.objects.create(
            name='Ksenia_Test2',
            surname='Kolomiets_Test2',
            date_of_birth='1981-01-29')
        student3 = Student.objects.create(
            name='Ksenia_Test3',
            surname='Kolomiets_Test3',
            date_of_birth='1981-01-29')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "next >>")


    def test_student_create(self):
        student1 = Student.objects.create(
            name='Ksenia',
            surname='Kolomiets',
            date_of_birth='1981-01-29')
        self.assertEqual(Student.objects.all().count(), 1)


class StudentsDetailTest(TestCase):
    def test_page_students_detail(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

        student1 = Student.objects.create(
            name='Ksenia',
            surname='Kolomiets',
            date_of_birth='1981-01-29')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Ksenia")
        #self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_students_detail_name_surname_in_header(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ksenia_Test Kolomiets_Test")

    def test_students_detail_birth_date_format(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jan. 29, 1981")

    def test_students_detail_email_displaying(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29',
            email="ksenia.k@gmail.com")
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ksenia.k@gmail.com")

    def test_students_detail_address_displaying(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29',
            address="Kharkov, Novgorodskaya, 11",)
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kharkov, Novgorodskaya, 11")

"""
        student1 = Student.objects.create(
            name='Ksenia_Test',
            surname='Kolomiets_Test',
            date_of_birth='1981-01-29',
            address="Kharkov",
            email="ksenia.k@gmail.com",
            phone="12-34-67",
            skype="ksenia")

        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ksenia_Test Kolomiets_Test")
        self.assertContains(response, "Jan. 29, 1981")
        self.assertContains(response, "Kharkov")
        self.assertContains(response, "ksenia.k@gmail.com")
        self.assertContains(response, "12-34-67")
        self.assertContains(response, "ksenia")
"""