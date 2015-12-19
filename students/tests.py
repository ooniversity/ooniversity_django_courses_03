from django.test import TestCase
from students.models import Student
from courses.models import Course


class StudentsListTest(TestCase):
    def test_courses_response_status(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_add_valid_student(self):
        response = self.client.get('/students/add/')
        self.assertContains(response, 'Student registration')

    def test_edit_valid_course(self):
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12'
        )
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_form.html')

    def test_remove_valid_student(self):
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12'
        )
        response = self.client.post('/students/remove/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 404)

    def test_title_form_list(self):
        response = self.client.get('/students/')
        self.assertContains(response, '<h5 class="white-text">Задайте вопрос</h5>')


class StudentsDetailTest(TestCase):
    def test_response_404(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_response_200(self):
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12'
        )
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(student.pk, 1)
        self.assertContains(response, 'Frank Sinatra')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_add_course(self):
        course = Course.objects.create(
            name='Python/Django 3 Поток',
            short_description='Изучать Python',
        )
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12',
        )
        student.courses.add(course)
        response = self.client.get('/students/1/')
        self.assertContains(response, '/courses/1/')

    def test_bursa_mail(self):
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12',
        )
        response = self.client.get('/students/1/')
        self.assertContains(response, 'itbursa100@gmail.com')

    def test_title_form(self):
        student = Student.objects.create(
            name='Frank',
            surname='Sinatra',
            date_of_birth='1915-12-12',
        )
        response = self.client.get('/students/1/')
        self.assertContains(response, '<h5 class="white-text">Задайте вопрос</h5>')
