from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from courses.models import Course, Lesson
from django.contrib import messages
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class StudentListView(ListView):
	model = Student
	template_name = 'students/list.html'
	context_object_name = 'students'
	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id')
		if course_id:
			qs = qs.filter(courses = course_id)
		return qs
				
class StudentDetailView(DetailView):
	model = Student
	template_name = 'students/detail.html'

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = u"Student registration"
		return context

	def form_valid(self, form):
		message = super(StudentCreateView, self).form_valid(form)
		mess = u'Student {} {} has been successfully added.' .format(self.object.name, self.object.surname)
		messages.success(self.request, mess)
		return message

class StudentUpdateView(UpdateView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = u"Student info update"
		return context

	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})
	def form_valid(self, form):
		message = super(StudentUpdateView, self).form_valid(form)
		messages.success(self.request, u'Info on the student has been sucessfully changed.')
		return message

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = u"Student info suppression"
		context['full_name'] = self.object.name + ' ' + self.object.surname
		return context

	def delete(self, request, *args, **kwargs):
		message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
		mess = u'Info on {} {} has been sucessfully deleted.' .format(self.object.name, self.object.surname)
		messages.success(self.request, mess)
		return message
