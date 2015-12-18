from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
import logging

logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return context

    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course_detail'


class CourseCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = 'Course %(name)s has been successfully added.' % {'name': name}
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)

    model = Course
    success_url = reverse_lazy("index")
    template_name = 'courses/add.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        course_id = self.kwargs['pk']
        return reverse('courses:edit', kwargs={'pk': course_id})

    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'


class CourseDeleteView(DeleteView):
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        name = course.name
        message = "Course %(name)s has been deleted." % {'name': name}
        messages.success(self.request, message)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    model = Course
    success_url = reverse_lazy("index")
    template_name = 'courses/remove.html'
    context_object_name = 'course'


class MixinLessonMessage(object):
    def form_valid(self, form):
        name = form.cleaned_data['subject']
        message = 'Lesson %(name)s has been successfully added.' % {'name': name}
        messages.success(self.request, message)
        return super(MixinLessonMessage, self).form_valid(form)


class LessonCreateView(MixinLessonMessage, CreateView):
    def get_initial(self):
        course_id = self.kwargs['pk']
        course = Course.objects.get(pk=course_id)
        return {'course': course.id}

    model = Lesson
    template_name = 'courses/add_lesson.html'
