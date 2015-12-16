from django.test import TestCase
from courses.models import Course

class CoursesListTest(TestCase):

    def test_course_create(self):
        course = Course.objects.create(name="Python")
        self.assertEqual(Course.objects.all().count(), 1)

    def test_lessons_create(self):
        course1 = Course.objects.create(name="Python")
        lesson1 = Lesson.objects.create(subject="Les1",course=course1,description="xfvdvdfv", order = 1)
        course1_lessons = Lesson.objects.filter(course_id=course1.id)
        self.assertEqual(course1_lessons.all().count(),1)
