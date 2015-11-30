from django.shortcuts import render
from courses.models import *
import os


# Create your views here.
def detail(request, request_id):
    course = Course.objects.get(id=request_id)
    lesson = Lesson.objects.filter(course=request_id)
    result = {
        'course': course,
        'lessons': lesson,
        'coach': course.coach.full_name(),
        'assistant': course.assistant.full_name(),
        'coach_id': course.coach.id,
        'assistant_id':course.assistant.id,
        'coach_desc': course.coach.description,
        'assistant_desc':course.assistant.description,
    }
    return render(
        request,
        os.path.join('courses', 'detail.html'),
        result
    )
