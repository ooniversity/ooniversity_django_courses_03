from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses = Course.objects.get(id = course_id))
        else:
            students = Student.objects.all()
        return students

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        messages.success(self.request, "Student " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + " has been successfully added.")
        return super(StudentCreateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    
    def form_valid(self, form):
        messages.success(self.request, "Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
