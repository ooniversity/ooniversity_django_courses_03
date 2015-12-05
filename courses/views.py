from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
	course = Course.objects.get(pk=course_id)
	lesson = Lesson.objects.all()
	return render(request, 'courses/detail.html', {'course':course, "lesson": lesson})

def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			messages.success(request, "Course %s has been succesfully added." % course.name)
		return redirect('index')
	form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return render(request, 'students/edit.html', {'form': form})

    form = CourseModelForm(instance=course)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course %s has been deleted." % course.name)
        return redirect('index')

    return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, course_id):
    course = Course.objects.get(id = course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been succesfully added." % lesson.subject)
        return redirect('courses:detail', course_id)
    form = LessonModelForm(initial = {'course': course.id})
    return render(request, 'courses/add_lesson.html', {'form': form} )