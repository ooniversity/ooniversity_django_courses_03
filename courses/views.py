from django.shortcuts import render
from courses.models import Course, Lesson

def courses(request):

    return render(request, 'index_course.html', {{'Course': Course}})
