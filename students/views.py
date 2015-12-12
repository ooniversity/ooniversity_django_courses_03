from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from students.models import Student
from courses.models import  Course, Lesson
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class StudentListView(ListView):

    model = Student
    context_object_name = "students"

    def get_queryset(self):
        students = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course.id', None)
        if course_id:
            students = Student.objects.filter(courses = course_id)
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
        self.object = form.save()
        message = 'Student %s %s has been successfully added.' %(form['name'].value(), form['surname'].value())
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):

    model = Student
    success_url = reverse_lazy('students:list_view')


    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        self.object = form.save()
        message = "Info on the student has been sucessfully changed."
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView ):

    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        messages.success(self.request, u'Info on %s %s has been successfully deleted.'
						%(self.object.name, self.object.surname))
        return super(StudentDeleteView, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        message_to_send = u'Info on {} {} has been sucessfully deleted.' .format(self.object.name, self.object.surname)
        messages.success(self.request, message_to_send)
        return message