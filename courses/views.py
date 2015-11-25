from django.shortcuts import render
from courses.models import Course, Lesson

# Create your views here.

def detail (request, course_id):
       return render (request, 'courses/detail.html')


