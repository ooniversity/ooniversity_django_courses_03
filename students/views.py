# -*- coding:UTF-8 -*-

from students.models import Student
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy


class StudentListView(ListView):
    model = Student
    # context_object_name = "students_list"

    def get_queryset(self):
        students_list = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students_list = students_list.filter(courses__id=course_id)
        return students_list


class StudentDetailView(DetailView):
    model = Student
    # template_name = ""
    # context_object_name = "student_details"


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Student registration'
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        message = u"Student %s %s has been successfully added." % (name, surname)
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    # redirect to the same edit page is implemented in models.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Student info update'
        return context

    def form_valid(self, form):
        message = u'Info on the student has been sucessfully changed.'  # successfully
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Student info suppression'
        return context

# good solution https://stackoverflow.com/a/25325228

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        message = u"Info on %s has been sucessfully deleted." % student  # successfully
        messages.success(self.request, message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
