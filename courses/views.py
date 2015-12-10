# -*- coding:UTF-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs.get(self.pk_url_kwarg, None))
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Course %s has been successfully added.' % (data['name']))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        data = form.instance
        messages.success(self.request, 'The changes have been saved.')
        self.success_url = reverse('courses:edit', args=(data.id,))
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    fields = '_all__'
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, 'Course %s has been deleted.' % (course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            text = u'Lesson %s has been successfully added.' % lesson.subject
            messages.success(request, text)
            return redirect('courses:detail', lesson.course.id)
    else:
        form = LessonModelForm()
    return render(request, "courses/add_lesson.html", {'form': form})
