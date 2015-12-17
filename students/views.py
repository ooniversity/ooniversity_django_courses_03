# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from students.forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses__id=course_id)
		return qs
	def get_context_data(self, **kwargs):
		context = super(StudentListView, self).get_context_data(**kwargs)
		context['course_id'] = self.request.GET.get('course_id', None)
		return context

'''
def list_view(request):
	if request.GET.get('course_id'):
		stud = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		stud = Student.objects.all()
	return render(request, 'students/list.html', {'students': stud})
'''


class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        return context	

'''
def detail(request, pk):
	return render(request, 'students/detail.html', {'student': Student.objects.get(id=pk)})
'''

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

'''
def add(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
			messages.success(request, mess)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})
'''

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

'''
def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Info on the student has been sucessfully changed.')
			return redirect('students:edit',  application.id)
	else:
		form = StudentModelForm(instance=application)
	return render(request, 'students/edit.html', {'form': form})
'''

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

'''
def remove(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
		messages.success(request, mess)
		return redirect('students:list_view')
    return render(request, 'students/remove.html', {'full_name': application.name+ ' ' +application.surname})
'''
