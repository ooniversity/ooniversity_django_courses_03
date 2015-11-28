# -*- coding: utf-8 -*-
from django.shortcuts import render
from students.models import Student
from courses.models import Course, Lesson

def list_view(request):
    #print $_COOKIE["__utmz"]
    if request.GET.get('course_id'):
        data_student = Student.objects.filter(courses = request.GET.get('course_id'))
    else:
        data_student = Student.objects.all()
    return render(request, 'students/list.html', {'students': data_student})

def detail(request, detail_id):
    return render(request, 'students/detail.html', {'student': Student.objects.get(id = detail_id)})
