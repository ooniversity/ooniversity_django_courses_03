# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson, Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__) #courses.views

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        courses = Course.objects.get(id=self.kwargs['pk'])
        context['course'] = courses
        if courses.coach:
            context['coach'] = courses.coach.user.get_full_name()
        if courses.assistant:
            context['assistant'] = courses.assistant.user.get_full_name()

        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")

        return context

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        context['name_form'] = "Создание нового курса"
        context['name_button'] = "Создать"
        return context

    def form_valid(self, form):
        form = super(CourseCreateView, self).form_valid(form)
        message = u'Course {} has been successfully added.' .format(self.object.name)
        messages.success(self.request, message)
        return form

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        context['name_form'] = "Редактирование данных курса"
        context['name_button'] = "Изменить"
        return context

    def form_valid(self, form):
        message = u'The changes have been saved.'
        messages.success(self.request, message)
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args = (self.object.pk,))

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        courses = Course.objects.get(id=self.kwargs['pk'])
        context['name'] = courses
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        mess = u'Course {} has been deleted.' .format(self.object.name)
        messages.success(self.request, mess)
        return message

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'

    def form_valid(self, form):
        message = super(LessonCreateView, self).form_valid(form)
        mess = u'Lesson {} has been successfully added.' .format(self.object.subject)
        messages.success(self.request, mess)
        return message

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.object.course_id})
