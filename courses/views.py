from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
import models
from forms import *

def detail(request,course_id):
    course =  get_object_or_404(Course, pk=course_id)
    return render(request, 'detail.html', {'course': course})

def create(request):
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Course " + form.cleaned_data['name'] + " has been successfully added."
            messages.success(request, text)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    sd = Course.objects.get(id=course_id)
    form = CourseModelForm(instance=sd)
    if request.POST:
        form = CourseModelForm(request.POST, instance=sd)
        if form.is_valid():
            form.save()
            text = "The changes have been saved."
            messages.success(request, text)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    cd = Courses.objects.get(id=course_id)
    if request.POST:
        text = "Course " + str(sd) + " has been deleted."
        messages.success(request, text)
        sd.delete()
        return redirect('courses:list_view')
    return render(request, 'index')

def add_lesson(request, course_id):
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            less = form.save()
            text = "Lesson " + form.cleaned_data['subject'] + " has been successfully added."
            messages.success(request, text)
            return redirect('courses:detail', less.course.id)
    else:
        cd = Course.objects.get(id=course_id)
        form = LessonModelForm(initial={'course': cd})
    return render(request, 'courses/add_lesson.html', {'form': form})
