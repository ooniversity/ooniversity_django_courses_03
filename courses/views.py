from django.shortcuts import render,  get_object_or_404
from courses.models import Course

def detail(request,course_id):
    course =  get_object_or_404(Course, pk=course_id)
    return render(request, 'detail.html', {'course': course})
