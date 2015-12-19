from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from datetime import date
from django.test import Client
from students.models import Student
from courses.models import Course
from students.views import StudentListView, StudentDetailView



def create_students():
    first_course = Course.objects.create(name = 'first_course', 
								         short_description = 'descr',
								         description = 'descr')
    
    second_course = Course.objects.create(name = 'second_course', 
								          short_description = 'descr',
								          description = 'descr')
								    

    third_course = Course.objects.create(name = 'third_course', 
								         short_description = 'descr',
								         description = 'descr')
								    
    first_student = Student.objects.create(name = 'first_student',
								           surname = 'Surname',
								           date_of_birth = date.today(),
								           email = 'first_student@mail.ru',
								           phone = '00000',
								           address = 'addr',
								           skype = 'skype')

    second_student = Student.objects.create(name = 'second_student',
								           surname = 'Surname',
								           date_of_birth = date.today(),
								           email = 'second_student@mail.ru',
								           phone = '00000',
								           address = 'addr',
								           skype = 'skype')

    third_student = Student.objects.create(name = 'third_student',
								           surname = 'Surname',
								           date_of_birth = date.today(),
								           email = 'third_student@mail.ru',
								           phone = '00000',
								           address = 'addr',
								           skype = 'skype')

    
    first_student.courses.add(first_course)
    second_student.courses.add(second_course)
    third_student.courses.add(third_course)


class StudentsListTest(TestCase):

    def test_student_list(self):
        self.assertEqual(resolve('/students/').func.__name__, 
            StudentListView.as_view().__name__)

    def test_status_code(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_html_content(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, '<h2>Students list</h2>')

    
    def test_context(self):
        client = Client()
        create_students()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_edit_student_url(self):
        client = Client()
        create_students()
        response = client.get('/students/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/students/edit/{}/"'.format(i))


class StudentsDetailTest(TestCase):

    def test_detail_template(self):
        create_students()
        for i in range(1, 4):
            self.assertEqual(
                resolve('/students/{}/'.format(i)).func.__name__, 
                		StudentDetailView.as_view().__name__            )
    
    def test_404_student(self):
        client = Client()
        response = client.get(reverse('students:detail', args=(1, )))
        self.assertEqual(response.status_code, 404)

    
    def test_detail(self):
        create_students()
        client = Client()
        for i in range(1, 4):
            response = client.get(reverse('students:detail', args=(i,)))
            self.assertEqual(response.status_code, 200)

    
    def test_detail_content(self):
        client = Client()
        create_students()
        response = client.get(reverse('students:detail', args=(1,)))
        self.assertTemplateUsed(response, 'students/student_detail.html')
        self.assertContains(response, '<h1>Student details</h1>')


    def test_detail_context(self):
        client = Client()
        create_students()
        response = client.get(reverse('students:detail', args=(1,)))
        student = response.context['object']
        self.assertEqual(student.name, 'first_student')