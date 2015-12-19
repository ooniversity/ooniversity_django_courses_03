from django.test import TestCase, Client
from students.models import Student


def create_student(st_name):
    Student.objects.create(
        name = st_name,
        surname = "surname",
        date_of_birth = "2010-10-10",
        email = "abc@test.com",
        phone = "1234567890",
        address = "bryklin 23",
        skype = "23232323",
        )


class StudentsListTest(TestCase):

    def test_list_statuscode(self):
        client = Client()
        responce = client.get('/students/')
        self.assertEqual(responce.status_code, 200)
        
    def test_list_header(self):
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'Student\'s list:')

    def test_list_url_active(self):
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, '<li class="active"><a href="/students/">Students</a></li>')

    def test_create_content(self):
        create_student('Xyz')
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, '123')

    def test_pagination(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'next >>')

    
class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student('Xyz')
        client = Client()
        responce = client.get('/students/1/')
        self.assertContains(responce, 'Xyz')
                
    def test_detail_statuscode(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/1/')
        self.assertEqual(responce.status_code, 200)

    def test_detail_redirect(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/2')
        self.assertEqual(responce.status_code, 301)

    def test_detail_header(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/1/')
        self.assertContains(responce, 'student\'s card ')

    def test_detail_url_active(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/1/')
        self.assertContains(responce, '<li class="active"><a href="/students/">Students</a></li>')

    def test_detail_content(self):
        for i in ['1', '2', '3', '4', '5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/5/')
        self.assertContains(responce, '5 123')


