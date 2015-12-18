# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Course, Lesson
from coaches.models import Coach
from courses.forms import LessonModelForm
from django.contrib import messages
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
import logging


logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    fields = '__all__'
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['title'] = context['course'].name
        course_id = context['course'].id
        context['lessons'] = Lesson.objects.filter(course__exact=course_id)
        try:
            context['coach'] = Coach.objects.get(coach_courses__exact=course_id)
        except ObjectDoesNotExist:
            context['coach'] = False
        try:
            context['assistant'] = Coach.objects.get(assistant_courses__exact=course_id)
        except ObjectDoesNotExist:
            context['assistant'] = False
        return context


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['form_name'] = 'Course creation'
        context['title'] = 'Course creation'
        context['button_text'] = 'Добавить'
        context['button_class'] = 'waves-effect waves-light btn cyan'
        return context

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, 'Course %s has been successfully added.' % course.name)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'form'

    def get_success_url(self):
        course = super(CourseUpdateView, self).get_context_data()
        success_url = reverse_lazy('courses:edit', kwargs={'course_id': course['form'].id})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['form_name'] = 'Course update'
        context['title'] = 'Course update'
        context['button_text'] = 'Редактировать'
        context['button_class'] = 'waves-effect waves-light btn'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    fields = '__all__'
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['form_name'] = 'Course deletion'
        context['remove_message'] = 'Warning, the course %s will be removed!' % context['course'].name
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, 'Course %s has been deleted.' % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson.subject)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm()
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)
