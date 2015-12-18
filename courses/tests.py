from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.models import User

def lesson_course(topic):
    return Lesson.objects.create(
        topic=topic,
        description='LessonDescription',
        index=1)

class CoursesListTest(TestCase):
    def test_course_list(self): 
        from django.test import Client
        client = Client()

        course1 = Course.objects.create(
            name = 'FakeCourseName1',
            short_description='CourseShortDescription1',
            description='CourseDescription1',
            ) 

        course2 = Course.objects.create(
            name = 'FakeCourseName2',
            short_description='CourseShortDescription2',
            description='CourseDescription2',
            ) 

        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Course.objects.all().count(), 2)

        for item in Course.objects.all():
            self.assertContains(response, item.name.upper())

        for item in Course.objects.all():
            self.assertContains(response, item.short_description)

        self.assertEqual(response.context['courses'][0].name, course1.name) 
        self.assertEqual(response.context['courses'][1].name, course2.name) 

        self.assertEqual(response.context['courses'][0].short_description, course1.short_description) 
        self.assertEqual(response.context['courses'][1].short_description, course2.short_description) 
        
class CoursesDetailTest(TestCase):
    def test_course_detail(self):
        from django.test import Client
        client = Client()

        response = client.get(reverse(
                                'courses:detail', 
                                args=(1,)))
        self.assertEqual(response.status_code, 404) 

        self.user1 = User.objects.create(username='CoachUserName1')
        self.user2 = User.objects.create(username='CoachUserName2')

        coach1 = Coach.objects.create(
            user=self.user1,
            date_of_birth=datetime.date(1901, 2, 13),
            gender='M',
            phone='0007',
            address='address1',
            skype='skype1',
            description='coach1 description')

        coach2 = Coach.objects.create(
            user=self.user2,
            date_of_birth=datetime.date(1981, 2, 22),
            gender='M',
            phone='2131232',
            address='address2',
            skype='skype2',
            description='coach2 description')

        course1 = coach1.rel_coaches.create(
            name = 'FakeCourseName1',
            short_description='CourseShortDescr',
            description='CourseDescription',
            ) 

        coach2.rel_assistants.add(course1)

        lesson1 = Lesson.objects.create(
            description='lesson1Description',
            course=course1,
            index = 1)

        lesson2 = Lesson.objects.create(
            description='lesson2Description',
            course=course1,
            index = 2)

        response = client.get(reverse(
                                 'courses:course', 
                                 args=(Course.objects.get().pk,)))

        self.assertEqual(response.status_code, 200)    
        self.assertTrue('object' in response.context)

        self.assertContains(response, course1.name)
        self.assertContains(response, course1.description)
        
        self.assertEqual(response.context['object'].pk, course1.pk)   
        self.assertEqual(response.context['object'].name, 
                         course1.name)

        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(Coach.objects.all().count(), 2)
        self.assertEqual(Lesson.objects.all().count(), 2)

        for item in Lesson.objects.all():
            self.assertContains(response, item.description)

        for item in User.objects.all():
            self.assertContains(response, item.get_full_name())

        for item in Coach.objects.all():
            self.assertContains(response, item.description)

        self.assertEqual(response.context['object'].trainer.user, self.u1)
        self.assertEqual(response.context['object'].assistant.user, self.u2)
