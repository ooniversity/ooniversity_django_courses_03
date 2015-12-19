from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course

class StudentsListTest(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_students_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_page_fails(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_create_student(self):
        self.assertEqual(Student.objects.all().count(), 2)

    def test_student_list_template(self):
        client = Client()
        create_student()
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

class StudentsDetailTest(TestCase):

    def test_detail_name(self):
        client = Client()
        create_student()
        response = self.client.get('/students/1/')        
        self.assertContains(response, '1')

    def test_student_html01(self):
        response = self.client.get('/students/1/')
        self.assertContains(response, '<td>Address</td>')

    
    def test_contacts(self):
		client = Client()
		response = client.get('/contact/')
		self.assertEqual(response.status_code, 200)

    
    def test_feedbacks(self):
		client = Client()
		response = client.get('/feedback/')
		self.assertEqual(response.status_code, 200)


    def test_index(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)


