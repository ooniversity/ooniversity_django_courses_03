from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    context ={}
    context['courses'] = Course.objects.all()
    return render(request, 'index.html', context)


def detail(request, course_id):
    p = get_object_or_404(Course, pk = course_id)
    context ={}
    context['lessons'] = Lesson.objects.filter(course_id=course_id)
    context['course'] = Course.objects.get(id=course_id)
    context['assistant'] = Coach.objects.get(assistant_courses=course_id)
    context['coach'] = Coach.objects.get(coach_courses=course_id)
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data
            course_add = form.save()
            message = 'Course %s has been successfully added.'  % course_add.name
            messages.success(request, message)
            return redirect('courses:index')
    else:
        form = CourseModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)
# Create your views here.


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            message = "The changes have been saved."
            messages.success(request, message)
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course':  course}
    if request.method == "POST":
        message = "Course %s has been deleted." % course.name
        course.delete()
        messages.success(request, message)
        return redirect('index')
    return render(request, 'courses/remove.html', context)


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = 'Lesson %s has been successfully added.' % form['subject'].value()
            messages.success(request, message)
            return redirect('courses:detail', course_id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)