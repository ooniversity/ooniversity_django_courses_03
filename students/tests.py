from django.test import TestCase, Client
from students.models import Student
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy

class StudentsListTest(TestCase):

    def test_student_create(self):
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        self.assertEqual(Student.objects.all().count(), 1)

    #def test_lessons_create(self):
    #    course1 = Course.objects.create(name="Python")
    #    lesson1 = Lesson.objects.create(subject="Les1",course=course1,description="xfvdvdfv", order = 1)
    #    course1_lessons = Lesson.objects.filter(course_id=course1.id)
    #    self.assertEqual(course1_lessons.all().count(),1)
    def test_list_statuscode(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertEqual(responce.status_code, 200)
    def test_list_url_active(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertContains(responce, '<li class="active"><a href="/students/">Students</a></li>')
    def test_list_header(self):
        client = Client()
        responce = client.get(reverse_lazy('students:list_view'))
        self.assertContains(responce, 'Students')
    def test_create_content(self):
        student1 = Student.objects.create(name="Katya",date_of_birth = '2015-01-01')
        client = Client()
        responce = client.get('/students/')
        self.assertContains(responce, 'Katya')
