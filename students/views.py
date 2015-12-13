from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from students.forms import StudentModelForm
from courses.models import Course
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator



class StudentListView(ListView):
    model = Student
    paginate_by = 2
    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
    def form_valid(self, form):
        context = super(StudentCreateView, self).form_valid(form)
        message = "Student %s %s has been successfully added."  %(self.object.name, self.object.surname)
        messages.success(self.request, message)
        return context

class StudentUpdateView(UpdateView):
    model = Student
    def get_success_url(self):
        context= reverse_lazy('students:edit', kwargs={'pk':self.object.pk})
        return context
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
    def form_valid(self, form):
        context = super(StudentUpdateView, self).form_valid(form)
        message = "Info on the student has been sucessfully changed."
        messages.success(self.request, message)
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
    def delete(self, request, *args, **kwargs):
        context = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        message = "Info on %s %s has been successfully deleted." %(self.object.name, self.object.surname)
        messages.success(self.request, message)
        return context
    