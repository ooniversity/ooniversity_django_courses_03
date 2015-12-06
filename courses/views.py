from django.shortcuts import render, redirect
from courses.models import *
from courses.forms import *
from django.contrib import messages
import os


# Create your views here.

def detail(request, request_id):
    course_id = Course.objects.get(id=request_id)
    
    result = {
    	'course': course_id,
    	'lessons': Lesson.objects.filter(course=request_id),
    	'coach': course_id.coach.full_name(),
	   	'assistant': course_id.assistant.full_name(),
	   	'coach_id': course_id.coach.id,
	   	'assistant_id':course_id.assistant.id,
        'coach_desc': course_id.coach.description,
        'assistant_desc': course_id.assistant.description,
	}
    return render(request, os.path.join('courses', 'detail.html'), result)


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course_add = form.save()
            messages.success(request,
                    'Course %s has been successfully added' % (course_add.name)
            )
            return redirect('index')
    else:
        form = CourseModelForm()

    data = {'form': form}

    return render(request,
                os.path.join('courses', 'add.html'),
                data)


def edit(request, request_id):
    course = Course.objects.get(id=request_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', request_id)
    else:
        form = CourseModelForm(instance=course)

    data = {'form': form}
    return render(request,
        os.path.join('courses', 'edit.html'),
        data)


def remove(request, request_id):
    course = Course.objects.get(id=request_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request,
            'Course %s has been deleted.' % (course.name))
        return redirect('index')

    message = 'Are you sure you want to remove %s course?' % (course.name)

    data = {'err_message': message}
    return render(request,
            os.path.join('courses', 'remove.html'),
            data
            )


def add_lesson(request, request_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_add = form.save()
            messages.success(request,
                    'Lesson %s has been successfully added.'% (lesson_add.subject))
            return redirect('courses:detail', request_id)
    else:
        form = LessonModelForm(initial={'course': request_id})

    data = {'form': form}
    return render(request, os.path.join('courses', 'add_lesson.html'), data)
