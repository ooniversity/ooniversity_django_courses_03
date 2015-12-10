from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentListView(ListView):
  template_name = "students/list.html"
  model = Student
  context_object_name = "students" 
  def get_queryset(self):
    course_id = self.request.GET.get('course_id', None)
    if course_id:
      students = Student.objects.filter(courses__id = course_id)
    else:
      students = Student.objects.all()
    return students
 
class StudentDetailView(DetailView):
  template_name = "students/detail.html"
  model = Student
  def get_context_data(self, **kwargs):
    context = super(StudentDetailView,self).get_context_data(**kwargs)
    context['courses'] = Course.objects.filter(student__id = self.object.id)
    return context

class StudentCreateView(CreateView):
  form_class = StudentModelForm
  template_name = "students/add.html"
  model = Student
  success_url = reverse_lazy('students:list_view')
  def form_valid(self, form):
    form.save()
    messages.success(self.request, "Student %s %s has been successfully added." %(form.cleaned_data['name'], form.cleaned_data['surname']) )
    return super(StudentCreateView,self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(StudentCreateView,self).get_context_data(**kwargs)
    context['title'] = "Student registration"
    return context
  
class StudentUpdateView(UpdateView):
  form_class = StudentModelForm
  template_name = "students/edit.html"
  model = Student
  def form_valid(self, form):
    form.save()
    self.success_url = reverse_lazy('students:edit', kwargs={'pk':self.object.pk})
    messages.success(self.request, "Info on the student has been sucessfully changed.")
    return super(StudentUpdateView,self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(StudentUpdateView,self).get_context_data(**kwargs)
    context['title'] = "Student info update"
    return context
  
class StudentDeleteView(DeleteView):
  template_name = "students/remove.html"
  model = Student
  success_url = reverse_lazy('students:list_view')
  def get_context_data(self, **kwargs):
    messages.success(self.request, "Info on %s %s has been sucessfully deleted." %(self.object.name, self.object.surname)) 
    context = super(StudentDeleteView,self).get_context_data(**kwargs)
    context['title'] = "Student info suppression"
    return context
