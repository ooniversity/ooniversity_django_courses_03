from django.contrib import messages
from django.shortcuts import render, redirect

from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = course.lesson_set.all()
    return render(request, 'courses/detail.html', {'course': course, 'lesson': lesson})


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, u'Course %s has been successfuly added.' % new_course.name)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    our_course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=our_course)
        if form.is_valid():
            form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=our_course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    our_course = Course.objects.get(id=course_id)
    name = u"%s" % our_course.name
    if request.method == 'POST':
        our_course.delete()
        messages.success(request, u'Course %s has been deleted.' % our_course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'name': name})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, u'Lesson %s has been successfuly added.' % new_lesson.subject)
            return redirect('courses:detail', new_lesson.course.id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
