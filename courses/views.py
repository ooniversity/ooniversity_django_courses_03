from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, id):
    course = Course.objects.get(id=id)
    lessons = course.lesson_set.all()
    return render(request, "courses/detail.html", {"course": course, "lessons": lessons})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course_new = form.save()
            message = u'Course %s has been successfully added.' %course_new.name
            messages.success(request, message)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})

def edit(request, id):
    course_edit = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course_edit)
        if form.is_valid():
            course_edit = form.save()
            message = "The changes have been saved."
            messages.success(request, message)
            return redirect('courses:edit', id)
    else:
    	form = CourseModelForm(instance=course_edit)
    return render(request, "courses/edit.html", {'form': form})

def remove(request, id):
    course_del = Course.objects.get(id=id)
    if request.method == 'POST':
        course_del.delete()
        message = "Course %s has been deleted." %course_del.name
        messages.success(request, message)
        return redirect('index')
    return render(request, "courses/remove.html", {"course_name": course_del.name})

def add_lesson(request, id):
    
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_new = form.save()
            message = 'Lesson %s has been successfully added.' %lesson_new.subject
            messages.success(request, message)
            return redirect("courses:detail", id)
    else:
        form = LessonModelForm(initial={'course': id})
    return render(request, "courses/add_lesson.html", {'form': form})