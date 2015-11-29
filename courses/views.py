from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, r_id):
    params={}
    params['course']= Course.objects.get(id = r_id)
    params['lessons']= Lesson.objects.filter(course = r_id)
    params['coach'] = Coach.objects.get(coach_courses = r_id)
    params['assistant'] = Coach.objects.get(assistant_courses = r_id)
    return render(request, 'courses/detail.html', params)
