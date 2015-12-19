from django.test import TestCase
from students.models import Student


# Create your tests here.
class StudentsListTest(TestCase):
    def test_student_create(self):
        student1 = Student.objects.create(
            name='Ksenia',
            surname='Kolomiets',
            date_of_birth='1981-01-29')
        self.assertEqual(Student.objects.all().count(), 1)


class StudentsDetailTest(TestCase):
    def test_pages(self):
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