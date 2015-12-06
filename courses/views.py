# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm
from django.contrib import messages
from courses.forms import LessonModelForm


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

'''
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
'''


def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            name = lesson.subject
            message = "Lesson %(name)s has been successfully added." % {'name': name}
            messages.success(request, message)
            return redirect("courses:detail", course.id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, "courses/add_lesson.html", {'form': form})