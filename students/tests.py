from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.

def load_test_data():

    course_A = Course.objects.create(
                            name='A',
                            short_description='short_d_a',
                            description='description_A')

    course_B = Course.objects.create(
                            name='B',
                            short_description='short_d_B',
                            description='description_B')

    student_A = Student.objects.create(
                            name='name1',
                            surname='surname1',
                            date_of_birth='1999-01-01',
                            email='A@example.com',
                            phone='1234',
                            address='addr1',
                            skype='skype1')
    student_A.courses.add(course_A)

    student_B = Student.objects.create(
                            name='name2',
                            surname='surname2',
                            date_of_birth='1999-01-02',
                            email='B@example.com',
                            phone='1235',
                            address='addr2',
                            skype='skype2')
    student_B.courses.add(course_B)

class StudentsListTest(TestCase):
    def setUp(self):
        self.client = Client()
        load_test_data()

    def test_students_count(self):
        self.assertEqual(Student.objects.all().count(), 2)

    def test_student_no_crash(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_is_correct_template(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_links_exists(self):
        response = self.client.get('/students/')
        for i in [1, 2]:
            self.assertContains(response, '/students/{}/'.format(i))
            self.assertContains(response, '/students/edit/{}/'.format(i))
            self.assertContains(response, '/students/remove/{}/'.format(i))

    def test_student_title(self):
            response = self.client.get('/students/')
            self.assertContains(response, '<title>ItBursa students</title>' )

class StudentsDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        load_test_data()

    def test_student_no_crash(self):
        for i in [1, 2]:
            response = self.client.get('/students/{}/'.format(i))
        self.assertEqual(response.status_code, 200)

    def test_student_not_found(self):
        response = self.client.get('/students/999/')
        self.assertEqual(response.status_code, 404)

    def test_student_is_correct_template(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_mail(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'A@example.com')

    def test_student_phone(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '1234')
