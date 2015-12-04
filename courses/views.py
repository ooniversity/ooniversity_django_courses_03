# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
    #return HttpResponse('course_id = {}'.format(course_id))
    args = {}
    #args['id'] = course_id        
    course = Course.objects.get(id=course_id)
    args['name'] = course.name
    args['description'] = course.description
    args['lesson1'] = Lesson.objects.filter(course__id=course_id)
    args['course_id'] = course_id
    #args['xuy'] = 'http://127.0.0.1:8000/students/?course_id={}'.format(course_id)
    args['coach_name'] = course.coach.name
    args['coach_surname'] = course.coach.surname
    args['coach_description'] = course.coach.description
    args['assistant_name'] = course.assistant.name
    args['assistant_surname'] = course.assistant.surname
    args['assistant_description'] = course.assistant.description
    args['coach'] = course.coach
    args['assistant'] = course.assistant


    #course.coach.coach_courses.select_related('coach_courses') - курсы тренера


    return render(request, 'courses/detail.html', args)

def add(request):
    args = {}
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid:
            form.save()
            data = form.cleaned_data
            name = data['name']
            messages.success(request, 'Course %s has been successfully added.' % (name))
            return redirect('index')
        else:
            form = CourseModelForm(request.POST)
            args['form'] = form
            return render(request, 'courses/add.html', args)
    else:
        form = CourseModelForm()
        args['form'] = form
        return render(request, 'courses/add.html', args)

def edit(request, course_id):
    args = {}
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect ('courses:edit', course_id=course_id)
        else:
            form = StudentModelForm(request.POST, instance=course)
            args['form'] = form
            return render(request, 'students/add.html', args)
    else:
        form = CourseModelForm(instance=course)
        args['form'] = form
        return render(request, 'courses/edit.html', args)

def remove(request, course_id):
    args = {}
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % (course.name))
        return redirect ('index')
    else:
        args['course'] = course
        return render(request, 'courses/remove.html', args)

def add_lesson(request, course_id):
    args = {}
    course = Course.objects.get(id=course_id)
    #lesson = Lesson.objects.get(course = course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            
            messages.success(request, 'Lesson %s has been successfully added.' % (data['subject']))
            return redirect ('courses:detail', course_id=course_id)
        else:
            #form = StudentModelForm(request.POST)
            args['form'] = form
            return render(request, 'students/add.html', args)
    else:
        form = LessonModelForm(initial={'course': course})
        args['form'] = form
        return render(request, 'courses/add_lesson.html', args)        

