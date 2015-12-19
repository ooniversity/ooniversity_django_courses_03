from django.test import TestCase
from students.models import Student

# Create your tests here.
class StudentsListTest(TestCase):
    def test_200_error(self):
        student1 = Student.objects.create(
            name = 'Ivan',
            surname = 'Ivanov',
            date_of_birth = '2000-01-01')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_appearance(self):
        student1 = Student.objects.create(
            name = 'Ivan',
            surname = 'Ivanov',
            date_of_birth = '2000-01-01')
        response = self.client.get('/students/')
        self.assertContains(response, 'Ivan Ivanov')

    def test_students_count(self):
        student1 = Student.objects.create(
            name = 'Ivan',
            surname = 'Ivanov',
            date_of_birth = '2000-01-01')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_students_empty(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'List is empty')

    def test_student_add(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Add')
