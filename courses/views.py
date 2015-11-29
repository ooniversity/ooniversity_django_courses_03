from django.shortcuts import render
from courses.models import *
from coaches.models import *
import os

# Create your views here.

def detail(request, request_id):
    result = {
    	'item': Course.objects.get(id=request_id),
    	'course': Course.objects.get(id=request_id),
    	'lessons': Lesson.objects.filter(course=request_id),
    	'coaches': Coach.objects.filter(coach_courses=request_id),
    	'assistants': Coach.objects.filter(assistant_courses=request_id)}

    return render(request, os.path.join('courses', 'detail.html'), result)