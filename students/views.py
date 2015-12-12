from students.models import Student, Course
from django.shortcuts import get_object_or_404, render, redirect
from students.forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentCreateView(CreateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, "Student %s %s has been successfully added." % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Info on the student has been sucessfully changed")
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        success_message = "Info on %s %s has been sucessfully deleted." % (self.object.name, self.object.surname)
        messages.success(self.request, success_message)
        return message