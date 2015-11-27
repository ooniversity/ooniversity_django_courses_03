# -*- coding: utf-8 -*- 
from django.shortcuts import render
from courses.models import Course, Lesson
#from coaches.models import Coach

def detail(request, pk):
    return render(request, 'courses/detail.html', {'course' : Course.objects.get(id=pk)})

"""
class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course
"""