from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, num):
    item = Course.objects.get(id=num)
    lesson = Lesson.objects.filter(course=Course.objects.filter(id=num))
    coaches = Coach.objects.filter(coach_courses=num)
    assistants = Coach.objects.filter(assistant_courses=num)
    return render(request, 'courses\detail.html', {'item': item, 'lesson': lesson,
                                                   'coaches': coaches, 'assistants': assistants
                                                   })


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            text = "Course %s has been successfully added." % course.name
            messages.success(request, text)
            return redirect('index')

    form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            text = "The changes have been saved."
            messages.success(request, text)
            return render(request, 'courses/edit.html', {'form': form})
    form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        text = "Course %s has been deleted." % course.name
        messages.success(request, text)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            text = "Lesson %s has been successfully added." % lesson.subject
            messages.success(request, text)
            return redirect('courses:detail', pk)

    course = Course.objects.get(id=pk)
    lesson = Lesson(course=course)
    form = LessonModelForm(instance=lesson)
    return render(request, 'courses/add_lesson.html', {'form': form})



