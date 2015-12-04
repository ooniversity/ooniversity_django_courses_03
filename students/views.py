from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from students.models import Student
from courses.models import Course, Lesson
from django.views.generic import ListView, DetailView
from django.views import generic

#class DetailView(generic.DetailView):
    #model = Student
    #template_name = 'students_list.html'

class IndexView(generic.ListView):
    template_name = 'student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all()



