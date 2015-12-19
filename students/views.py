# -*- coding:UTF-8 -*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.db import models
from django.core.paginator import Paginator
from django.views.generic.list import *
import models
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
import logger
logger=logging.getlogger(__name__)

class StudentListView(ListView):
    model = Student
    paginate_by = 2
    #paginator = Paginator(super(StudentListView, self).get_queryset())
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id = course_id)
        return qs
    context_object_name = 'student_list'

class StudentDetailView(DetailView):
    model = Student
    success_url = reverse_lazy('index')
    logger.debug("Students detail view has been debugged")
    logger.info("Logger of students detail view informs you")
    logger.warning("Logger of students detail view warns you")
    logger.error("Students detail view went wrong!")
    # student = models.Student.objects.get(id = student_id)
    # return render(request, 'students/detail.html', {'student': student})

class StudentCreateView(CreateView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context
    success_url = reverse_lazy('students:list_view')

class StudentDeleteView(DeleteView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context
    success_url = reverse_lazy('students:list_view')


def create(request):
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = u"Студент " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + u" успешно добавлен"
            messages.success(request, text)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    sd = Student.objects.get(id=student_id)
    form = StudentModelForm(instance=sd)
    if request.POST:
        form = StudentModelForm(request.POST, instance=sd)
        if form.is_valid():
            form.save()
            text = "Информация о студенте успешно изменена"
            messages.success(request, text)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    sd = Student.objects.get(id=student_id)
    if request.POST:
        text = "Информация о " + str(sd) + " была успешно удалена"
        messages.success(request, text)
        sd.delete()
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'sd': sd})
