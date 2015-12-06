from django.shortcuts import render
from courses.models import Course
from django.shortcuts import get_object_or_404
from courses.forms import CourseModelForm, LessonModelForm
from django.shortcuts import redirect
from django.contrib import messages


def detail(request, pk):
    course_object =  get_object_or_404(Course, pk=pk) 
    return render(request, 'courses/detail.html', {'course_object': course_object})


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course %s has been successfully added." % (course.name))
            return redirect('index')
        else:
            form = CourseModelForm(request.POST)
            return render(request, 'courses/add.html', {'form':form})
    else:
        form = CourseModelForm()
        return render(request, 'courses/add.html', {'form':form})


def edit(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', pk=pk)
        else:
            form = CourseModelForm(request.POST, instance=course)
            return render(request, 'courses/edit.html', {'form':form})
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form':form})


def remove(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." % (course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    if request.method == "POST":
        form = LessonModelForm(request.POST, initial={'course': pk})
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." % (lesson.subject))
            return redirect('courses:detail', pk=pk)
        else:
            form = LessonModelForm(request.POST, initial={'course': pk})
            return render(request, 'courses/add_lesson.html', {'form':form})
    else:
        form = LessonModelForm(initial={'course': pk})
        return render(request, 'courses/add_lesson.html', {'form':form})
