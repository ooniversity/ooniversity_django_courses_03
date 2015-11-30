from django.shortcuts import render
from coaches.models import *
from courses.models import *
import os

# Create your views here.

def detail(request, request_id):
    result = {
    	'teacher': Coach.objects.get(id=request_id),
    	'course_coach': Course.objects.filter(coach_id=request_id),
    	'course_assistant': Course.objects.filter(assistant_id=request_id),
    }
    return render(request, os.path.join('coaches', 'detail.html'), result)