 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    context_object_name = "course"
    template_name = "courses/add.html"
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        context['button_name'] = "Создать"
        return context

    def form_valid(self, form):
        message = super(CourseCreateView, self).form_valid(form)
        success_message = "Course %s has been successfully added." % self.object.name
        messages.success(self.request, success_message)
        return message

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    def form_valid(self, form):
        message = super(CourseUpdateView, self).form_valid(form)
        success_message = "The changes have been saved."
        messages.success(self.request, success_message)
        return message
    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        context['button_name'] = "Сохранить"
        return context

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("index")
    template_name = "courses/remove.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        context['button_name'] = "Удалить"
        messages.success(self.request, "Course %s has been deleted." % self.object.name)
        return context

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson.subject)
            return redirect('courses:detail', course_id)
    else:
    	form = LessonModelForm(initial = {'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form} )
