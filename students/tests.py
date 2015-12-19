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
