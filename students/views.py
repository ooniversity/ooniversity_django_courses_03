from django.contrib import messages
from django.shortcuts import render, redirect
from students.models import Student
from django.core.urlresolvers import reverse_lazy
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


class StudentDetailView(DetailView):
    model = Student



class StudentListlView(ListView):
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        qs = super(StudentListlView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(course=course_id)
        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_add')

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
    success_url = reverse_lazy('students:student_add')
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
    success_url = reverse_lazy('students:student_add')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        message = u"Info on %s has been successfully deleted." % student  # successfully
        messages.success(self.request, message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)







