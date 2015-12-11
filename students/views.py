from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentListView(ListView):
	model = Student

	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses=course_id)
		return qs

class StudentDetailView(DetailView):
	model = Student
	success_url = 'students:list_view'

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def form_valid(self, form):
		data = form.cleaned_data
		msg = 'Student %s %s has been successfully added.' % (data['name'], data['surname'])
		messages.success(self.request, msg)
		return super(StudentCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Student registration'
		return context

class StudentUpdateView(UpdateView):
	model = Student

	def form_valid(self, form):
	    msg = 'Info on the student has been sucessfully changed.'
	    messages.success(self.request, msg)
	    return super(StudentUpdateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Student info update'
		return context

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Student info suppression'
		msg = 'Info on %s %s has been sucessfully deleted.' % (self.object.name, self.object.surname)
		messages.success(self.request, msg)

		return context
