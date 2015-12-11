from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class CourseDetailView(DetailView):
	model = Course
	template_name = "courses/detail.html"
	success_url = 'courses:detail'
	context_object_name = "course"

class CourseCreateView(CreateView):
	model = Course
	success_url = reverse_lazy('index')
	template_name = "courses/add.html"
	context_object_name = "form"

	def form_valid(self, form):
		data = form.cleaned_data
		messages.success(self.request, 'Course %s has been successfully added.' % (data['name']))
		return super(CourseCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Course creation'
		return context

class CourseUpdateView(UpdateView):
	model = Course
	template_name = "courses/edit.html"
	context_object_name = "form"


    def form_valid(self, form):
    	data = form.instance
    	messages.success(self.request, 'The changes have been saved.')
    	self.success_url = reverse('courses:edit', args=(data.id,))
    	return super(CourseUpdateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Course update'
		return context

class CourseDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('index')
	template_name = "courses/remove.html"
	context_object_name = "course"

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Course deletion'

		return context

	def delete(self, request, *args, **kwargs):
		course = super(CourseDeleteView, self).get_object()
		messages.success(request, "Course %s has been deleted." % (course.name))
		return super(CourseDeleteView, self).delete(request, *args, **kwargs)

class LessonCreateView(CreateView):
	model = Lesson
	template_name = 'courses/add_lesson.html'

	def get_context_data(self, **kwargs):
		context = super(LessonCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Lesson creation'
		return context

	def form_valid(self, form):
		data = form.cleaned_data
		messages.success(self.request, 'Lesson %s has been successfully added.' % (data['subject']))
		return super(LessonCreateView, self).form_valid(form)
