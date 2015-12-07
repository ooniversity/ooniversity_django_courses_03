from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
import os


# Create your views here.
def detail(request, pk):
    course = Course.objects.get(id=pk)
    lesson = Lesson.objects.filter(course=pk)

    content = {
        'course': course,
        'lessons': lesson,
        'coach': course.coach.full_name(),
        'assistant': course.assistant.full_name(),
        'coach_id': course.coach.id,
        'assistant_id': course.assistant.id,
        'coach_desc': course.coach.description,
        'assistant_desc': course.assistant.description,
    }
    return render(request, os.path.join('courses', 'detail.html'), content)


def add(request):
    # if request.POST:
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course {0} has been successfully added.'.format(course.name))
            # form.save()
            # messages.success(request, 'Course {0} has been successfully added.'.format(form.cleaned_data['name']))
            return redirect('index')
    else:
        form = CourseModelForm()

    context = {'form': form}
    return render(request, os.path.join('courses', 'add.html'), context)


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid:
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance=course)

    context = {'form': form}
    return render(request, os.path.join('courses', 'edit.html'), context)


def remove(request, pk):
    course = Course.objects.get(id=pk)
    notification = 'Are you sure you want to remove {0} course?'.format(course.name)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course {0} has been deleted.'.format(course.name))
        return redirect('index')

    context = {'notification': notification}
    return render(request, os.path.join('courses', 'remove.html'), context)


def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(lesson.subject))
            # form.save()
            # messages.success(request, 'Lesson {0} has been successfully added.'.format(form.cleaned_data['subject']))
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial={'course': pk})

    context = {'form': form}
    return render(request, os.path.join('courses', 'add_lesson.html'), context)
