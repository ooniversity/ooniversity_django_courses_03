 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator

class StudentListView(ListView):
	model = Student
	paginate_by = 2
	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			student = Student.objects.filter(courses = course_id)
		else:
			student = Student.objects.all()
		return student
	def get_context_data(self, **kwargs):
		context = super(StudentListView, self).get_context_data(**kwargs)
		course_id = self.request.GET.get('course_id', None)
		if self.request.GET.get('course_id', None):
			context['course_id'] = "course_id=%s&" % course_id
		else:
			context['course_id'] = ""
		return context

class StudentDetailView(DetailView):
	model = Student

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		context['button_name'] = "Создать"
		return context

	def form_valid(self, form):
		message = super(StudentCreateView, self).form_valid(form)
		success_message = "Student %s %s has been successfully added." %(self.object.name, self.object.surname)
		messages.success(self.request, success_message)
		return message

class StudentUpdateView(UpdateView):
	model = Student
	def form_valid(self, form):
		message = super(StudentUpdateView, self).form_valid(form)
		success_message = "Info on the student has been sucessfully changed."
		messages.success(self.request, success_message)
		return message
	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		context['button_name'] = "Сохранить"
		return context

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy("students:list_view")

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		context['button_name'] = "Удалить"
		messages.success(self.request, "Info on %s has been sucessfully deleted." % self.object.fullname())
		return context