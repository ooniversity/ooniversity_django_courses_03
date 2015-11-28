from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):

       course_id = Course.objects.get(id=course_id)

       lessons = Lesson.objects.filter(course=course_id) 

       return render(request, 'courses/detail.html',  {'course': course_id, 'lessons': lessons})