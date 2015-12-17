# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student
from courses.models import Course, Lesson
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator

import logging
logger = logging.getLogger(__name__) #students.views

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
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id:
            qs = qs.filter(courses = course_id)
        return qs

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        context['name_form'] = "Создание нового студента"
        context['name_button'] = "Создать"
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            application = form.save()
            message = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
            messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    #success_url = reverse_lazy('students:list_view')
    #template_name = 'students/student_update.html'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        context['name_form'] = "Редактирование данных студента"
        context['name_button'] = "Изменить"
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            application = form.save()
            message = u'Info on the student has been sucessfully changed.'
            messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args = (self.object.pk,))

class StudentDeleteView(DeleteView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        application = Student.objects.get(id=self.kwargs['pk'])
        context['name'] = application.name
        context['surname'] = application.surname
        return context

    def get_success_url(self, **kwargs):
        application = Student.objects.get(id=self.kwargs['pk'])
        if self.request.method == 'POST':
            application.delete()
            message = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
            messages.success(self.request, message)
            return reverse_lazy('students:list_view')
        return reverse_lazy('students:remove')

