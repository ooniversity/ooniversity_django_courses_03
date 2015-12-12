from django.shortcuts import render
from coaches.models import *
from courses.models import *
import os

# Create your views here.

def detail(request, pk):
    result = {
    	'teacher': Coach.objects.get(id=pk),
    	'course_coach': Course.objects.filter(coach_id=pk),
    	'course_assistant': Course.objects.filter(assistant_id=pk),
    }
    return render(request, os.path.join('coaches', 'detail.html'), result)