from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages



def index(request):

    courses_list = Course.objects.all()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'courses_list': courses_list,
    })
    return HttpResponse(template.render(context))


def couse_detail(request, course_id):

    course = Course.objects.get(pk = course_id)
    lessons_list = Lesson.objects.filter(course = course)
    template = loader.get_template('courses/detail.html')
    context = RequestContext(request, {
        'course': course,
        'lessons_list': lessons_list
    })
    return HttpResponse(template.render(context))


# Add
def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            c_name = form.data.get('name')
            messages.success(request, 'Course %s has been successfully added.'% c_name)
            return redirect('index')

    template = loader.get_template('courses/add.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))


# add_lesson
def add_lesson(request, pk):

    course = Course.objects.get(id=pk)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            l_name = form.cleaned_data['subject']
            messages.success(request, 'Lesson %s has been successfully added.'% l_name)
            return redirect('courses:course_detail', course_id=pk)

    template = loader.get_template('courses/add_lesson.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))


# Delete
def remove(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        c_name = course.name
        course.delete()
        messages.success(request, 'Course %s has been deleted.'% c_name)
        return redirect('index')

    template = loader.get_template('courses/remove.html')
    context = RequestContext(request, {
        'course': course
    })
    return HttpResponse(template.render(context))


# Edit
def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk=pk)
    else:
        form = CourseModelForm(instance=course)

    template = loader.get_template('courses/edit.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))