# -*- coding:UTF-8 -*-

from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
    courseId = request.GET.get('course_id', None)
    if courseId:
        students = Student.objects.filter(courses=Course.objects.get(id=courseId))
    else:
        students = Student.objects.all()
    cl = Course.objects.all()
    return render(request, 'students/list.html', {'students_list': students, 'courses_list': cl})


def detail(request, student_id):
    sd = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student_detail': sd})
