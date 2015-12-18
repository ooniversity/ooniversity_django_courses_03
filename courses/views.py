# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        return context
    

'''
def detail(request, pk):
    return render(request, 'courses/detail.html', {'course': Course.objects.get(id=pk)})
'''

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    #success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Lesson creation"
        return context

    def form_valid(self, form):
        message = super(LessonCreateView, self).form_valid(form)
        mess = u'Lesson {} has been successfully added.' .format(self.object.subject)
        messages.success(self.request, mess)
        return message

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.object.course_id})


'''
def add_lesson(request, pk):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = u'Lesson {} has been successfully added.' .format(application.subject)
			messages.success(request, mess)
			return redirect('courses:detail', application.course.id)
	else:
		form = LessonModelForm()
	return render(request, 'courses/add_lesson.html', {'form': form})
'''


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Course creation"
        return context

    def form_valid(self, form):
        message = super(CourseCreateView, self).form_valid(form)
        mess = u'Course {} has been successfully added.' .format(self.object.name)
        messages.success(self.request, mess)
        return message

'''
def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = u'Course {} has been successfully added.' .format(application.name)
			messages.success(request, mess)
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})
'''

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        message = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, u'The changes have been saved.')
        return message

'''
def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'The changes have been saved.')
			return redirect('courses:edit',  application.id)
	else:
		form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'form': form})
'''

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        mess = u'Course {} has been deleted.' .format(self.object.name)
        messages.success(self.request, mess)
        return message

'''
def remove(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = u'Course {} has been deleted.' .format(application.name)
		messages.success(request, mess)
		return redirect('index')
    return render(request, 'courses/remove.html', {'name': application.name})
'''
