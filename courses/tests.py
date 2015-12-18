# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from pybursa.views import IndexView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

class CoursesListTest(TestCase):
    
    """
    def setUp(self):
        User.objects.create(username='user', password='user')
        Course.objects.create(name='course1', short_description='1short_description', description='1description')
        Coach.objects.create(
            user = User.objects.get(username='user'), date_of_birth = '2012-10-10',
            gender = 'M', phone = '1234567890', address = 'address',
            skype = 'skype', description = 'description')
        Course.objects.create(name='course2', short_description='2short_description', description='2description', coach_id=1)
    """
    def test_course_list_without_courses(self):
        from django.test import Client
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        

    def test_course_list_with_courses(self):
        from django.test import Client
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 0)
        course = Course.objects.create(name='course', short_description='short description')
        response = client.get('/')
        self.assertEqual(response.context['courses'].count(), 1)    
    

    def test_course_list_info(self):
        from django.test import Client
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        course = Course.objects.create(name='Course', short_description='short description')
        response = client.get('/')
        self.assertContains(response, course.name.upper())
        self.assertContains(response, course.short_description.title())
    
    
    def test_course_list_filters(self):
        from django.test import Client
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        course = Course.objects.create(name='Course', short_description='short')
        response = client.get('/')
        #self.assertContains(response, course.name.upper())
        self.assertNotContains(response, course.name)
        self.assertNotContains(response, course.short_description)    

    def test_course_list_links_detail(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        course = Course.objects.create(name='Course', short_description='short')
        response = client.get('/')
        ahref_detail = '<a href="/courses/%s/">%s</a>' % (course.id, course.name.upper())
        self.assertContains(response, ahref_detail)
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': course.id})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 200)
        
    def test_course_list_links_create(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short')    
        response = client.get('/')
        ahref_add = '<a href="/courses/add/'
        self.assertContains(response, ahref_add)
        link_add = reverse_lazy('courses:add')
        response = client.get(link_add)
        self.assertEqual(response.status_code, 200)
        


    def test_course_list_links_edit(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short')
        response = client.get('/')
        ahref_edit = '<a href="/courses/edit/%s/"' % course.id
        self.assertContains(response, ahref_edit)
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.get(link_edit)
        self.assertEqual(response.status_code, 200)
        
    def test_course_list_links_remove(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short')
        response = client.get('/')
        ahref_remove = '<a href="/courses/remove/%s/"' % course.id
        self.assertContains(response, ahref_remove)
        link_remove = reverse_lazy('courses:remove', kwargs={'pk': course.id})
        response = client.get(link_remove)
        self.assertEqual(response.status_code, 200)

    def test_course_create_is_info(self):
        from django.test import Client
        client = Client()
        link_add = reverse_lazy('courses:add')
        response = client.post(link_add, {'name': 'course', 'short_description': 'short_description', 'description': 'description'})
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(Course.objects.get(id=1).name, 'course')
        self.assertEqual(Course.objects.get(id=1).short_description, 'short_description')
        self.assertEqual(Course.objects.get(id=1).description, 'description')

    def test_course_create_redirect(self):
        from django.test import Client
        client = Client()
        link_add = reverse_lazy('courses:add')
        response = client.post(link_add, {'name': 'course', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertRedirects(response, '/', fetch_redirect_response=True)
        
    def test_course_create_message(self):
        from django.test import Client
        client = Client()
        link_add = reverse_lazy('courses:add')
        response = client.post(link_add, {'name': 'course', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertRedirects(response, '/', fetch_redirect_response=True)
        message = 'Course %s has been successfully added.' % (Course.objects.get(id=1).name)
        self.assertContains(response, message)
    
    def test_course_create_form(self):
        from django.test import Client
        client = Client()
        link_add = reverse_lazy('courses:add')
        response = client.post(link_add, {'name': '', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_add, {'name': 'course', 'short_description': '', 'description': 'description'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_add, {'name': 'course', 'short_description': 'short_description', 'description': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
    
    def test_course_create_context_is_title(self):
        from django.test import Client
        client = Client()
        link_add = reverse_lazy('courses:add')
        response = client.get(link_add)
        self.assertEqual(response.context['title'], 'Course creation')

    def test_course_update_is_info(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.post(link_edit, {'name': 'edited_course', 'short_description': 'short_description', 'description': 'description'})
        self.assertEqual(Course.objects.get(id=1).name, 'edited_course')
        self.assertEqual(Course.objects.get(id=1).short_description, 'short_description')
        self.assertEqual(Course.objects.get(id=1).description, 'description')
        response = client.post(link_edit, {'name': 'Course', 'short_description': 'edited short_description', 'description': 'description'})
        self.assertEqual(Course.objects.get(id=1).name, 'Course')
        self.assertEqual(Course.objects.get(id=1).short_description, 'edited short_description')
        self.assertEqual(Course.objects.get(id=1).description, 'description')
        response = client.post(link_edit, {'name': 'Course', 'short_description': 'short_description', 'description': 'edited description'})
        self.assertEqual(Course.objects.get(id=1).name, 'Course')
        self.assertEqual(Course.objects.get(id=1).short_description, 'short_description')
        self.assertEqual(Course.objects.get(id=1).description, 'edited description')
        response = client.post(link_edit, {'name': 'edited Course', 'short_description': 'edited short_description', 'description': 'edited description'})
        self.assertEqual(Course.objects.get(id=1).name, 'edited Course')
        self.assertEqual(Course.objects.get(id=1).short_description, 'edited short_description')
        self.assertEqual(Course.objects.get(id=1).description, 'edited description')

    def test_course_update_redirect(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.post(link_edit, {'name': 'edited course', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertRedirects(response, '/courses/edit/%s/' % course.id, fetch_redirect_response=True)    
            
    def test_course_update_message(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.post(link_edit, {'name': 'edited course', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertRedirects(response, '/courses/edit/%s/' % course.id, fetch_redirect_response=True)
        message = 'The changes have been saved.'
        self.assertContains(response, message)    

    def test_course_update_form(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.post(link_edit, {'name': '', 'short_description': 'short_description', 'description': 'description'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_edit, {'name': 'edited course', 'short_description': '', 'description': 'description'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_edit, {'name': 'edited course', 'short_description': 'short_description', 'description': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

    def test_course_update_context_is_title(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_edit = reverse_lazy('courses:edit', kwargs={'pk': course.id})
        response = client.get(link_edit)
        self.assertEqual(response.context['title'], 'Course update')

    def test_course_remove_is_work(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_remove = reverse_lazy('courses:remove', kwargs={'pk': course.id})
        response = client.post(link_remove)
        self.assertEqual(Course.objects.all().count(), 0)
        
    def test_course_remove_redirect(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_remove = reverse_lazy('courses:remove', kwargs={'pk': course.id})
        response = client.post(link_remove, follow=True)
        self.assertRedirects(response, '/' , fetch_redirect_response=True)

    def test_course_remove_message(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_remove = reverse_lazy('courses:remove', kwargs={'pk': course.id})
        response = client.post(link_remove, follow=True)
        self.assertRedirects(response, '/' , fetch_redirect_response=True)            
        message = 'Course %s has been deleted.' % (course.name)
        self.assertContains(response, message)

    def test_course_remove_context_is_title(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_remove = reverse_lazy('courses:remove', kwargs={'pk': course.id})
        response = client.get(link_remove)
        self.assertEqual(response.context['title'], 'Course deletion')    
    
    
class CoursesDetailTest(TestCase):
    
    def test_courses_detail(self):
        from django.test import Client
        client = Client()
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': 1})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 404)
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': course.id})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 200)

    def test_courses_detail_info_without_coaches(self):
        from django.test import Client
        client = Client()
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': 1})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 404)
        course = Course.objects.create(name='Course', short_description='short_description', description='description')
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': course.id})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course')
        #self.assertContains(response, 'short_description')
        self.assertContains(response, 'description')

    def test_courses_detail_info_with_coaches(self):
        from django.test import Client
        client = Client()
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': 1})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 404)
        User.objects.create(username='user', password='user', first_name='first', last_name='trener')
        User.objects.create(username='user2', password='user2', first_name='second', last_name='pomownik')
        coach = Coach.objects.create(
            user = User.objects.get(username='user'), date_of_birth = '2012-10-10',
            gender = 'M', phone = '1234567890', address = 'address',
            skype = 'skype', description = 'this is coach')
        assistant = Coach.objects.create(
            user = User.objects.get(username='user2'), date_of_birth = '2012-11-11',
            gender = 'M', phone = '1234567890', address = 'address',
            skype = 'skype', description = 'this is assistant')
        course = Course.objects.create(name='Course', short_description='short_description', description='description', coach_id=coach.id, assistant_id=assistant.id)
        
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': course.id})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course')
        #self.assertContains(response, 'short_description')
        self.assertContains(response, 'description')
        self.assertContains(response, 'first trener')
        self.assertContains(response, 'this is coach')
        self.assertContains(response, 'second pomownik')
        self.assertContains(response, 'this is assistant')

    def test_courses_detail_info_with_lessons(self):
        from django.test import Client
        client = Client()
        link_detail = reverse_lazy('courses:detail', kwargs={'pk': 1})
        response = client.get(link_detail)
        self.assertEqual(response.status_code, 404)
        User.objects.create(username='user', password='user', first_name='first', last_name='trener')
        User.objects.create(username='user2', password='user2', first_name='second', last_name='pomownik')
        coach = Coach.objects.create(
            user = User.objects.get(username='user'), date_of_birth = '2012-10-10',
            gender = 'M', phone = '1234567890', address = 'address',
            skype = 'skype', description = 'this is coach')
        assistant = Coach.objects.create(
            user = User.objects.get(username='user2'), date_of_birth = '2012-11-11',
            gender = 'M', phone = '1234567890', address = 'address',
            skype = 'skype', description = 'this is assistant')
        
        course = Course.objects.create(name='Course', short_description='short_description', description='description', coach_id=coach.id, assistant_id=assistant.id)
        course2 = Course.objects.create(name='Course2', short_description='short_description', description='description', coach_id=coach.id, assistant_id=assistant.id)
        
        lesson1 = Lesson.objects.create(subject='this first subject', description='this first lesson', course_id=course.id, order=1)
        lesson2 = Lesson.objects.create(subject='that first subject', description='that first lesson', course_id=course2.id, order=1)
        
        link_detail1 = reverse_lazy('courses:detail', kwargs={'pk': course.id})
        link_detail2 = reverse_lazy('courses:detail', kwargs={'pk': course2.id})
        
        response = client.get(link_detail1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course')
        #self.assertContains(response, 'short_description')
        self.assertContains(response, 'description')
        self.assertContains(response, 'first trener')
        self.assertContains(response, 'this is coach')
        self.assertContains(response, 'second pomownik')
        self.assertContains(response, 'this is assistant')
        self.assertEqual(course.lesson_set.all().count(), 1)
        self.assertContains(response, '1')
        self.assertContains(response, 'this first subject')
        self.assertContains(response, 'this first lesson')
        self.assertNotContains(response, 'that first lesson')
        response = client.get(link_detail2)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course2')
        #self.assertContains(response, 'short_description')
        self.assertContains(response, 'description')
        self.assertContains(response, 'first trener')
        self.assertContains(response, 'this is coach')
        self.assertContains(response, 'second pomownik')
        self.assertContains(response, 'this is assistant')
        self.assertEqual(course.lesson_set.all().count(), 1)
        self.assertContains(response, '1')
        self.assertContains(response, 'that first subject')
        self.assertContains(response, 'that first lesson')
        self.assertNotContains(response, 'this first lesson')

    def test_course_detail_create_lesson(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        course2 = Course.objects.create(name='Course', short_description='short', description='description')
        link_add_lesson = reverse_lazy('courses:add-lesson', kwargs={'pk': course.id})
        link_add_lesson2 = reverse_lazy('courses:add-lesson', kwargs={'pk': course2.id})
        response = client.get(link_add_lesson)
        self.assertEqual(response.status_code, 200)
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': 'this first lesson', 'course': course.id, 'order': 1})
        self.assertEqual(Lesson.objects.all().count(), 1)
        self.assertEqual(course.lesson_set.all().count(), 1)
        response = client.post(link_add_lesson2, {'subject': 'this first subject', 'description': 'this first lesson', 'course': course2.id, 'order': 1})
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(course.lesson_set.all().count(), 1)
        

    
       
    def test_course_detail_create_lesson_redirect(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        link_add_lesson = reverse_lazy('courses:add-lesson', kwargs={'pk': course.id})
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': 'this first lesson', 'course': course.id, 'order': 1}, follow=True)
        self.assertRedirects(response, '/courses/%s/' % course.id, fetch_redirect_response=True)

        
    def test_course_detail_create_lesson_message(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        link_add_lesson = reverse_lazy('courses:add-lesson', kwargs={'pk': course.id})
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': 'this first lesson', 'course': course.id, 'order': 1}, follow=True)
        self.assertRedirects(response, '/courses/%s/' % course.id, fetch_redirect_response=True)
        message = 'Lesson %s has been successfully added.' % (course.lesson_set.filter(id=1).get().subject)
        self.assertContains(response, message)

    
    def test_course_deatil_create_lesson_form(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        link_add_lesson = reverse_lazy('courses:add-lesson', kwargs={'pk': course.id})
        response = client.post(link_add_lesson, {'subject': '', 'description': 'this first lesson', 'course': course.id, 'order': 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': '', 'course': course.id, 'order': 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': 'this first lesson', 'course': '', 'order': 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        response = client.post(link_add_lesson, {'subject': 'this first subject', 'description': 'this first lesson', 'course': course.id, 'order': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
    

    def test_course_detail_create_lesson_is_initial(self):
        from django.test import Client
        client = Client()
        course = Course.objects.create(name='Course', short_description='short', description='description')
        link_add_lesson = reverse_lazy('courses:add-lesson', kwargs={'pk': course.id})
        response = client.get(link_add_lesson)
        course_id = response.context['form'].initial['course'].id
        self.assertEqual(response.status_code, 200)
        self.assertEqual(course_id, course.id)    





            







           
            
        
"""
    <a href="/courses/1/">PYTHON&amp;DJANGO</a>

    def test_course_create(self):
        course1 = Course.objects.create(name='pybursa02', short_description='sfdsfdfbdf')
        self.assertEqual(Course.objects.all().count(), 3)

    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/3/')
        self.assertEqual(response.status_code, 404)
        course2 = Course.objects.create(name='pybursa02', short_description='sfdsfdfbdf', description='re')
        #coach = Coaches.objects.create(gender_choices='Male', use)
        response = client.get('/courses/3/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pybursa02')
"""

"""
from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse, reverse_lazy

class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject
    def get_absolute_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.course_id})



from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    gender_choices = (('M', 'Male'), ('F', 'Female'), )
 
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
    

    def __unicode__(self):
        return self.user.get_username()
    def get_name(self):
        return "%s" % (self.user.first_name)
    get_name.short_description = 'name'
    
    name = property(get_name)  

    def get_surname(self):
        return "%s" % (self.user.last_name)
    get_surname.short_description = 'surname'
    
    surname = property(get_surname)    
    def get_staff(self):
         return "%s" % (self.user.is_staff)
    def get_email(self):
        return "%s" % (self.user.email)
    get_email.short_description = 'email'
    email = property(get_email)

"""