from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

