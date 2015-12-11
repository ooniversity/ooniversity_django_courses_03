# -*- coding:UTF-8 -*-

import sys

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from courses.models import Course
from students.models import Student

reload(sys)
sys.setdefaultencoding('utf8')


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=Course.objects.get(id=course_id))
        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        context['button_text'] = "Добавить"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Студент %s %s успешно добавлен.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        context['button_text'] = "Изменить"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Данные изменены.')
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Студент %s %s был удален.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
