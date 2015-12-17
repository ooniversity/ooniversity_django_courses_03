# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.forms import StudentModelForm
from students.models import Student

import logging

logger = logging.getLogger(__name__)


"""
def list_view(request):
	try:
		id_course= request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
	return render(request,'students/list.html',{'name_stud': n_student})
"""	

class StudentListView(ListView):
	model = Student
	paginate_by = 2
	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses=course_id)
		return qs
		
	
class StudentDetailView(DetailView):
	model = Student
	logger.debug("Students detail view has been debugged")
	logger.info("Logger of students detail view informs you!")
	logger.warning("Logger of students detail view warns you!")
	logger.error("Students detail view went wrong!")
		

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
 		return context
	def form_valid(self, form):
		added_student = form.save()
		success_mes = 'Student %s %s has been successfully added' % (added_student.name, added_student.surname)
		messages.success(self.request, success_mes, extra_tags='msg')
		return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
	model = Student
	def get_success_url(self):
		return reverse('students:edit', kwargs={'pk': self.object.id})
	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
 		return context
	def form_valid(self, form):
		added_student = form.save()
		success_mes = 'Info on the student has been sucessfully changed.'
		messages.success(self.request, success_mes, extra_tags='msg')
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
 		return context
	def get_object(self):
		deleted_student = super(StudentDeleteView, self).get_object()
		messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (deleted_student.name, deleted_student.surname), extra_tags='msg')
		return deleted_student

