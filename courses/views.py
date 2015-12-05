# -*- coding: utf-8 -*- 
from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, courses_id):
    try:
        courses = get_object_or_404(Course, pk=courses_id)
        lessons = courses.lesson_set.all()
        return render(request, 'courses/detail.html', { 
                      'courses':courses , 
                      'lessons':lessons,
                      })
    except ObjectDoesNotExist:
        achtung = "Houston, we have a problem with id = {0} exist yet.".format(courses_id) 
	return render(request, 'courses/detail.html', {
		    "achtung": achtung,
            })

  
def add(request):
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST)
        if course_form.is_valid():
            course = course_form.save()
            messages.success(request, u"Course %s has been successfully added." % (course.name))
            return redirect('index')
    else:
        course_form = CourseModelForm()
    return render(request, 'courses/add.html', {
                  'course_form': course_form,
                  })


def edit(request, courses_id):
    course = Course.objects.get(id=courses_id)
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST, instance=course)
        if course_form.is_valid():
            course = course_form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', courses_id)
    else:
        course_form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {
                  'course_form': course_form,
                  })
    


def remove(request, courses_id): 
    course_remove = Course.objects.get(id=courses_id)
    remove_massage = u"Вы уверены, что хотите удалить информацию о %s ?" % (course_remove.name)
    if request.method == 'POST':
        course_remove.delete()
        messages.success(request, u"Course %s has been deleted." % (course_remove.name))
        return redirect('index')
    return render(request, 'courses/remove.html',{
                  'remove_massage': remove_massage,
                  })


def add_lesson(request, courses_id):
    if request.method == 'POST':
        lesson_form = LessonModelForm(request.POST)
        if lesson_form.is_valid():
            lessons = lesson_form.save()
            messages.success(request, u"Lesson %s has been successfully added." % (lessons.subject))
            return redirect('courses:detail', courses_id)
    else:
        lesson_form = LessonModelForm()
    return render(request, 'courses/add_lesson.html', {
                  'lesson_form': lesson_form,
                  })




         
