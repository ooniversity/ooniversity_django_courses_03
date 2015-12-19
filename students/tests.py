from django.test import TestCase, Client
from students.models import Student
from courses.models import Course


def create_data():
    course_1 = Course.objects.create(
        name='Python',
        short_description='Bla bla bla Python',
        description='Too many Bla bla bla Python')

    course_2 = Course.objects.create(
        name='Java',
        short_description='Bla bla bla Java',
        description='Too many Bla bla bla Java')

    student_1 = Student.objects.create(
        name='Tom',
        surname='Soyer',
        date_of_birth='1985-06-15',
        email='tom@email.com',
        phone='+380 67 111 11 11',
        address='address 1',
        skype='tomy',
    )
    student_2 = Student.objects.create(
        name='Bob',
        surname='Big',
        date_of_birth='1999-06-15',
        email='bb@email.com',
        phone='+380 97 111 11 11',
        address='address 2',
        skype='bigbob'
    )
    student_1.courses.add(course_1)
    student_2.courses.add(course_2)


class StudentsListTest(TestCase):
    def setUp(self):
        self.client = Client()
        create_data()

    def test_chek_list_random(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bob')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_chek_links(self):
        response = self.client.get('/students/')
        self.assertContains(response, '/students/1/')
        self.assertContains(response, '/students/edit/1/')
        self.assertContains(response, '/students/remove/2/')

    def test_check_valid_add_student(self):
        response = self.client.post('/students/add/', {'name':'Don', 'surname': 'Carlione',
                                                       'date_of_birth': '1999-06-15', 'email': 'bb@email.com',
                                                       'phone': '+380 97 111 11 11', 'address': 'address 3',
                                                       'skype': 'bigbob', 'courses': 'Python'})
        self.assertEqual(response.status_code, 200)

    def test_check_student_1(self):
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'address 1')
        self.assertContains(response, 'tom@email.com')

    def test_remove_students(self):
        for i in range(1, 2):
            response = self.client.post('/students/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 302)
            response = self.client.get('/students/remove/{}/'.format(i))
            self.assertEqual(response.status_code, 404)

    def test_count_student(self):
        self.assertEqual(Student.objects.all().count(), 2)


class StudentsDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        create_data()

    def test_student_detail(self):
        response = self.client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_student_check_mail_all(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'tom@email.com')
        response = self.client.get('/students/2/')
        self.assertContains(response, 'bb@email.com')

    def test_student_check_course(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Python')

    def test_student_skype_check(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, 'tomy')

    def test_student_check_phone(self):
        response = self.client.get('/students/2/')
        self.assertContains(response, '+380 97 111 11 11')
