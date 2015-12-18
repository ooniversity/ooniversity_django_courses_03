# -*- coding: utf-8 -*
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from students.models import Student
from students.forms import StudentModelForm
from django.views import generic

import logging
logger = logging.getLogger(__name__)

class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return super(StudentDetailView, self).get_context_data(**kwargs)

class StudentListView(ListView):
    model = Student
    paginate_by = 2
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (
            student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
            self.object.name, self.object.surname))
        return message
