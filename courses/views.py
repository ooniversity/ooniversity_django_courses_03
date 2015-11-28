# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
    return render(request, 'courses/detail.html', {'course': Course.objects.get(id = course_id)})
