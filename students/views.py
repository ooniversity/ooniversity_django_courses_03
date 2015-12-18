from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages
from students.forms import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import logging
logger = logging.getLogger(__name__) # students.view

class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context

class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        if 'course_id' in self.request.GET:
            student_list = Student.objects.filter(courses=self.request.GET['course_id'])
        else:
            student_list = Student.objects.all()
        return student_list


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        data['title'] = 'Student registration'
        return data

    def form_valid(self, form):
        student = form.save()
        mess = "Student {} {} has been successfully added.".format(student.name, student.surname)
        messages.success(self.request, mess)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentUpdateView, self).get_context_data(**kwargs)
        data['title'] = 'Student info update'
        return data

    def form_valid(self, form):
        form.save()
        mess = 'Info on the student has been sucessfully changed.'
        messages.success(self.request, mess)
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:edit', None, [self.object.id])


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def delete(self, request, *args, **kwargs):
        data = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        fname = '{} {}'.format(self.object.name, self.object.surname)
        mess = 'Info on {} has been sucessfully deleted.'.format(fname)
        messages.success(self.request, mess)
        return data