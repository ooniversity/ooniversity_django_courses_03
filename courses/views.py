# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm
from django.contrib import messages


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
