from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
from students.models import Student

def detail(request, c_id):
    params = {}
    params['teacher'] = get_object_or_404(Coach, pk=c_id)    
    params['course_coach'] = Course.objects.filter(coach_id = c_id)
    params['course_assistant'] = Course.objects.filter(assistant_id = c_id)
    template = 'coaches/detail.html'
    return render (request, template, params)
