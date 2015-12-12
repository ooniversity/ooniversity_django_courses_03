# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm
from django.contrib import messages
from courses.forms import LessonModelForm

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['title'] = u'Course details'
        context['lessons'] = Lesson.objects.filter(course=self.object)
        context['course_current'] = self.object
        context['course_name'] = self.object.name
        context['course_id'] = self.object.id
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Course creation'
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = u"Course %s has been sucessfully added." % name  # successfully
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)


# ---- old

def detail(request, course_id):
    course_id = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course_id)

    return render(request, 'courses/detail.html', {'course': course_id, 'lessons': lessons})


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course %s has been successfully added.' % (form.cleaned_data['name']))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." % course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, course_id):
    if request.method == "post":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            tmp = form.save()
            subject = tmp.subject
            messages.success(request, 'Lesson %s has been successfully added.' % subject)
            return redirect('courses:detail', form.cleaned_data['course'].id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
