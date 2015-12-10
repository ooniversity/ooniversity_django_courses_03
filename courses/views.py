# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson, Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        courses = Course.objects.get(id=self.kwargs['pk'])
        context['course'] = courses
        context['coach'] = courses.coach.user.get_full_name()
        context['assistant'] = courses.assistant.user.get_full_name()
        return context

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')

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

def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message = u'Lesson {} has been successfully added.' .format(application.subject)
            messages.success(request, message)
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'form': form})
