# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class StudentListView(ListView):
  model = Student
  paginate_by = 2
  def get_queryset(self):
    students = super(StudentListView, self).get_queryset()
    course_id = self.request.GET.get('course_id', None)
    if course_id:
      students = students.filter(courses = course_id)
    return students
  def get_context_data(self, **kwargs):
    context = super(StudentListView, self).get_context_data(**kwargs)
    course_id = self.request.GET.get('course_id', None)
    if course_id:
      context['course_id'] = course_id
    return context
 
class StudentDetailView(DetailView):
  model = Student
  def get_context_data(self, **kwargs):
    context = super(StudentDetailView,self).get_context_data(**kwargs)
    context['courses'] = Course.objects.filter(student__id = self.object.id)
    return context

class StudentCreateView(CreateView):
  form_class = StudentModelForm
  model = Student
  success_url = reverse_lazy('students:list_view')
  def form_valid(self, form):
    create_message = super(StudentCreateView, self).form_valid(form)
    messages.success(self.request, "Student %s %s has been successfully added." %(form.cleaned_data['name'], form.cleaned_data['surname']) )
    return create_message
  def get_context_data(self, **kwargs):
    context = super(StudentCreateView,self).get_context_data(**kwargs)
    context['title'] = "Student registration"
    return context
  
class StudentUpdateView(UpdateView):
  form_class = StudentModelForm
  model = Student
  def form_valid(self, form):
    update_message = super(StudentUpdateView, self).form_valid(form)
    messages.success(self.request, "Info on the student has been sucessfully changed.")
    return update_message
  def get_success_url(self):
    return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})
  def get_context_data(self, **kwargs):
    context = super(StudentUpdateView,self).get_context_data(**kwargs)
    context['title'] = "Student info update"
    return context
  
class StudentDeleteView(DeleteView):
  model = Student
  success_url = reverse_lazy('students:list_view')
  def get_context_data(self, **kwargs):
    context = super(StudentDeleteView, self).get_context_data(**kwargs)
    messages.success(self.request, "Info on %s %s has been sucessfully deleted." %(self.object.name, self.object.surname))
    context['title'] = "Student info suppression"
    return context