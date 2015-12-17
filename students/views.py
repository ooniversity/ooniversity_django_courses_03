# -*- coding: utf-8 -*-

from students.models import Student
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)

# Create your views here.


class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        return context


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id and course_id.isdigit():
            return Student.objects.filter(courses=course_id)
        return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        student = form.save()
        message = 'Student %s %s has been successfully added.' % (student.name, student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    # form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self, **kwargs):
        message = 'Info on the student has been sucessfully changed.'
        messages.success(self.request, message)
        return reverse_lazy('students:edit', args=(self.object.pk,))


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


