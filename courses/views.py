from django.shortcuts import render, redirect
from django.views import generic

from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, r_id):
    params={}
    params['course']= Course.objects.get(id = r_id)
    params['lessons']= Lesson.objects.filter(course = r_id)
    return render(request, 'courses/detail.html', params)

def add(request):
    params = {}
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned = form.cleaned_data
            messages.success(request, 'Course {0} has been successfully added.'.format(cleaned['name']))
            return redirect('index')
    else:
        form = CourseModelForm()
    params['form'] = form
    return render(request, 'courses/add.html', params)

def edit(request, c_id):
    params = {}
    course = Course.objects.get(id=c_id)
    if request.POST:
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', c_id)
    else:
        form = CourseModelForm(instance=course)
    params['form'] = form
    return render(request, 'courses/edit.html', params)

def remove(request, c_id):
    params = {}
    course = Course.objects.get(id = c_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course {0} has been deleted.".format(course.name))
        return redirect('index')
    params['course'] = course
    return render(request, 'courses/remove.html', params)

def add_lesson(request, c_id):
    params = {}
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(form.cleaned_data['subject']))
            return redirect('courses:detail', form.cleaned_data['course'].id)
    else:
        form = LessonModelForm(initial={ 'course' : c_id })
    params['form'] = form
    return render(request, 'courses/add_lesson.html', params)
