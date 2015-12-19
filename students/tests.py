from django.test import TestCase, Client
from students.models import Student


def create_student(st_name):
    Student.objects.create(
        name = st_name,
        surname = "Test2",
        date_of_birth = "2015-05-30",
        email = "test1@gmail.com",
        phone = "0631434750",
        address = "No adress",
        skype = "test1",
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
        create_student('Test_name_1')
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'Test_name_1')

    def test_pagination(self):
        for i in ['test1', 'test2', 'test3', 'test4', 'test5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'next >>')

    
class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student('Test1')
        client = Client()
        responce = client.get('/students/1/')
        self.assertContains(responce, 'Test1')
                
    def test_detail_statuscode(self):
        for i in ['T1', 'T2', 'T3', 'T4', 'T5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/1/')
        self.assertEqual(responce.status_code, 200)

    def test_detail_redirect(self):
        for i in ['T1', 'T2', 'T3', 'T4', 'T5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/2')
        self.assertEqual(responce.status_code, 301)

    def test_detail_url_active(self):
        for i in ['T1', 'T2', 'T3', 'T4', 'T5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/1/')
        self.assertContains(responce, '<li class="active"><a href="/students/">Students</a></li>')

    def test_detail_content(self):
        for i in ['T1', 'T2', 'T3', 'T4', 'T5']:
            create_student(i)
        client = Client()
        responce = client.get('/students/5/')
        self.assertContains(responce, 'T5 Test2')
