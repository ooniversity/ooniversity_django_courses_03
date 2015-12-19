from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        return context


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
        text = u'Course {0} has been successfully added.' .format(self.object.name)
        messages.success(self.request, text)
        return message

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
        text = u'Course {0} has been deleted.' .format(self.object.name)
        messages.success(self.request, text)
        return message

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Lesson creation"
        return context

    def form_valid(self, form):
        message = super(LessonCreateView, self).form_valid(form)
        text = u'Lesson {0} has been successfully added.' .format(self.object.subject)
        messages.success(self.request, text)
        return message

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.object.course_id})
