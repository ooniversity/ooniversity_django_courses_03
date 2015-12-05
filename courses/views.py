# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, pk):
    return render(request, 'courses/detail.html', {'course' : Course.objects.get(id=pk)})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            mess = 'Course {} has been successfully added.'.format(application.name)
            messages.success(request, mess)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})
    
def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit',  course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." % course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', { 'course': course })
    
def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            mess = 'Lesson {} has been successfully added.'.format(application.subject)
            messages.success(request, mess)
            return redirect('courses:detail', application.course.id)
    else:
        form = LessonModelForm()
    return render(request, 'courses/add_lesson.html', {'form': form})