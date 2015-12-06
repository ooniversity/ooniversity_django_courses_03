from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
    courses = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.all()
    coaches = Coach.objects.all()

    return render (request, 'courses/detail.html',{'courses':courses,'lessons':lessons, 'coaches': coaches})

def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Course {} has been successfully added.' .format(application.name)
			messages.success(request, message)
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'The changes have been saved.')
			return redirect('courses:edit', application.id)
	else:
		form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		message = u'Course {} has been sucessfully deleted.' .format(application.name)
		messages.success(request, message)
		return redirect('index')
    return render(request, 'courses/remove.html', {'name': application.name})

def add_lesson(request, pk):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Lesson {} has been successfully added.' .format(application.subject)
			messages.success(request, message)
			print application.course.id
			return redirect('courses:detail', application.course.id)
	else:
		form = LessonModelForm()
	return render(request, 'courses/add_lesson.html', {'form': form})
