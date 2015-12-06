from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    my_course = Course.objects.get(pk=course_id)
    my_lessons = Lesson.objects.filter(course=course_id)
    return render(request, "courses/detail.html", {'my_course': my_course, 'my_lessons': my_lessons})


def add(request):
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            course_form = course_form.cleaned_data            
            my_message = "Course {} has been successfully added.".format(course_form['name'])
            messages.success(request, my_message)
            return redirect ('index')
    else:
        course_form = CourseModelForm()        
    return render(request, "courses/add.html", {'course_form': course_form})

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            messages.success(request, 'The changes have been saved.')
    else:
        course_form = CourseModelForm(instance=course)
    return render(request, "courses/edit.html", {'course_form':course_form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    name = course.name
    if request.method == 'POST':
        course.delete()
        my_message = "Course {} has been deleted.".format(name)
        messages.success(request, my_message)
        return redirect ('index')
    return render(request, "courses/remove.html", {'name':name})


def add_lesson(request, course_id):
    if request.method == 'POST':
        lesson_form = LessonModelForm(request.POST)
        if lesson_form.is_valid():
            lesson_form.save()
            lesson_form = lesson_form.cleaned_data            
            my_message = "Lesson {} has been successfully added.".format(lesson_form['subject'])
            messages.success(request, my_message)
            return redirect ('courses:detail', course_id=course_id)
    else:
        lesson_form = LessonModelForm(initial={'course': course_id})        
    return render(request, "courses/add_lesson.html", {'lesson_form': lesson_form})
