from django.shortcuts import render

from courses.models import Course, Lesson


def detail (request, course_id):
       cd = Course.objects.get(id=course_id)
       ll = Lesson.objects.filter(course=course_id) 
       return render (request, 'courses/detail.html',  {'course_detail': cd, 'lessons_list': ll})

