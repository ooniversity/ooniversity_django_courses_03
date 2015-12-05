from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from polls.models import Choice, Question
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    course_lessons = Lesson.objects.filter(course_id = course_id)
    course_par = "?course_id=" + course_id
    return render(request, 'courses/detail.html', {'course_lessons': course_lessons, 'course': course, 'course_par': course_par})

def add(request):

    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            added_course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % added_course)
            return redirect('/')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {"form": form})

def add_lesson(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form =LessonModelForm(request.POST)
        if form.is_valid():
            added_lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % added_lesson)
            return redirect('courses:detail', course_id=course.id)
    else:
        form = LessonModelForm(initial={'course': course})

    return render(request, 'courses/add_lesson.html', {"form": form})

def edit(request, course_id):

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course_id = course.id)
    else:
        form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course)
        return redirect('/')

    return render(request, 'courses/remove.html', {'course': course})

