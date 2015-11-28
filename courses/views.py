from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson

def detail(request, r_id):
    params={}
    params['course']= Course.objects.get(id = r_id)
    params['lessons']= Lesson.objects.filter(course = r_id)
    return render(request, 'courses/detail.html', params)
