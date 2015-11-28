from django.shortcuts import render
from courses.models import *
import os


# Create your views here.
def detail(request, request_id):
    result = {
        'course': Course.objects.get(id=request_id),
        'lessons': Lesson.objects.filter(course=request_id)
    }
    return render(
        request,
        os.path.join('courses', 'detail.html'),
        result
    )