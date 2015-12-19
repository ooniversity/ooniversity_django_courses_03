from django.test import TestCase, Client
from students.models import Student

class StudentsListTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_create(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        self.assertEqual(Student.objects.all().count(), 1)


    def test_list_delete(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        student1.delete()
        self.assertEqual(Student.objects.all().count(), 0)


    def test_list_update(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        student1.surname ="Kravtsov"
        student1.save()
        response = self.client.get('/students/1/')
        self.assertContains(response, "Sergeenko")


    def test_student_list(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        response = self.client.get('/students/')
        self.assertContains(response, "Sergeenko")


    def test_attribute(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        self.assertTrue(student1.name)


class StudentsDetailTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_200_status(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)


    def test_non_existent_page(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)


    def test_detail_create(self):
        sstudent1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        response = self.client.get('/students/1/')
        self.assertContains(response, "Sergeenko")


    def test_template_used(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        with self.assertTemplateUsed('students/student_detail.html'):
            self.client.get('/students/1/')


    def test_detail_view(self):
        student1 = Student.objects.create(
            name="Ivan",
            surname="Sergeenko",
            date_of_birth='1985-11-07',
            email='ivan.sergeenko@gmail.com',
            phone='+3806712345678',
            address='Kharkov, Petrovskogo st. 67',
            skype='ivansg85')
        response = self.client.get('/students/')
        self.assertContains(response, "Sergeenko")
