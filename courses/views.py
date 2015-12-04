from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    lessons = courses.lesson_set.all()
    coaches = courses.coach.user.get_full_name()
    assistants = courses.assistant.user.get_full_name()
    return render(request,
                  'courses/detail.html', {
                      'courses': courses,
                      'lessons': lessons,
                      'coaches': coaches,
                      'assistants': assistants
                  })


def add(request):
    context = {}
    if request.method == "POST":
        context['form'] = form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Course %s has been successfully added.' % (
                data['name']))
            return redirect('index')

    else:
        context['form'] = CourseModelForm()
    return render(request, 'courses/add.html', context)


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(
                request, 'The changes has been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % (
            course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (
                 data['subject']))
            return redirect('courses:detail', data['course'].id)
    else:
        form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'form': form})
