# -*- coding: utf-8 -*-
from .models import Student
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging


logger = logging.getLogger(__name__)


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
        try:
            course_id = self.request.GET['course_id']
            students = Student.objects.filter(courses__exact=course_id)
        except:
            students = Student.objects.all()
        return students


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['form_name'] = 'Student registration'
        context['title'] = 'Add new student'
        context['button_text'] = 'Добавить'
        context['button_class'] = 'waves-effect waves-light btn cyan'
        return context

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

    def get_success_url(self):
        student = super(StudentUpdateView, self).get_context_data()
        success_url = reverse_lazy('students:edit', kwargs={'student_id': student['student'].id})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['form_name'] = 'Edit student'
        context['title'] = 'Student info update'
        context['button_text'] = 'Редактировать'
        context['button_class'] = 'waves-effect waves-light btn'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Information about the student has successfully changed')
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['remove_message'] = 'Warning, the student %s %s will be removed!' % (
            context['student'].name, context['student'].surname)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Attention, you're going to remove the student %s %s. Confirm the action" % (
            student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
