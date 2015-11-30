from django.shortcuts import render
from courses.models import *
from coaches.models import *
import os

# Create your views here.

def detail(request, request_id):
    course_id = Course.objects.get(id=request_id)
    result = {
    	'course': course_id,
    	'lessons': Lesson.objects.filter(course=request_id),
    	'coach': course_id.coach.full_name(),
	   	'assistant': course_id.assistant.full_name(),
	   	'coach_id': course_id.coach.id,
	   	'assistant_id':course_id.assistant.id,
	}
    return render(request, os.path.join('courses', 'detail.html'), result)
