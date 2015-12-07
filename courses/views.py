# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from coaches.models import Coach
from .models import Course
from django.core.exceptions import ObjectDoesNotExist
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.template.context import RequestContext
from django.core.context_processors import csrf


def detail(request, course_id):
    try:
        coach = Coach.objects.get(coach_courses__exact=course_id)
        assistant = Coach.objects.get(assistant_courses__exact=course_id)
    except ObjectDoesNotExist:
        coach = False
        assistant = False
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
        'coach': coach,
        'assistant': assistant,
    }
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % course.name)
            return redirect('index')
    else:
        form = CourseModelForm()
    context = {'form': form}
    context.update(csrf(request))
    return render(request, 'courses/add.html', context, context_instance=RequestContext(request))


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=course)
    context = {'form': form}
    context.update(csrf(request))
    return render(request, 'courses/edit.html', context, context_instance=RequestContext(request))


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    remove_message = 'Warning, the course %s will be removed ' % course.name
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course.name)
        return redirect('index')
    context = {'remove_message': remove_message}
    context.update(csrf(request))
    return render(request, 'courses/remove.html', context, context_instance=RequestContext(request))


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
    context.update(csrf(request))
    return render(request, 'courses/add_lesson.html', context, context_instance=RequestContext(request))
