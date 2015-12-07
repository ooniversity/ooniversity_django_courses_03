from courses.models import Course, Lesson
from django.shortcuts import get_object_or_404, render, redirect
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def main(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def detail(request, pk):
    course_object =  get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course_object': course_object})

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course %s has been successfully added." % (course.name))
            return redirect ('courses:list_view')
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
            return redirect ('courses:edit', pk=pk)
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
        return redirect ('courses:list_view')
    return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." % (lesson.name))
            return redirect ('courses:list_view')
        else:
            form = LessonModelForm(request.POST)
            return render(request, 'courses/detail.html', {'form':form})
    else:
        form = CourseModelForm()
        return render(request, 'courses/detail.html', {'form':form})
