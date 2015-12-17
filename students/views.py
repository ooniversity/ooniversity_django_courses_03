<<<<<<< HEAD
from django.shortcuts import redirect, render
from students.models import Student
from students import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.
import logging
logger = logging.getLogger(__name__)

class StudentDetailView(DetailView):
    model = Student
    logger.debug("Students detail view has been debugged")
    logger.info("Logger of students detail view informs you!")
    logger.warning("Logger of students detail view warns you!")
    logger.error("Students detail view went wrong!")


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        students_course = self.request.GET
        if 'course_id' in students_course:
            queryset = queryset.filter(courses=students_course['course_id'])
        return queryset
        

class StudentCreateView(CreateView):
    model = Student
    
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        student = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student['name'], student['surname']))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        student = self.get_object()
        messages.success(self.request, 'Info on the student %s %s has been sucessfully changed.' % (student.name, student.surname))
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, **kwargs):
        student = self.get_object()
        message = super(StudentDeleteView, self).delete(request, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return message
=======
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
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172



