from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

	
def detail(request, pk):
	course = Course.objects.get(id = pk)
	lessons = Lesson.objects.filter(course = pk)
	return render(request, 'courses/detail.html', {'course' : course, 'lessons' : lessons})
	
	
def create(request):
	if request.method == 'POST':	
		model_form = CourseModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			name = model_form.cleaned_data['name']
			messages.success(request, 'Course %s has been successfully added.' % (name))
			return redirect('index')
	else:
		model_form = CourseModelForm()
	return render(request, 'courses/add.html', {'model_form': model_form})
	
	
def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = CourseModelForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit', application.id)
	else:
		model_form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'model_form': model_form})
	

def remove(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()	
		messages.success(request, 'Course %s has been deleted.' % (application.name))
		return redirect('index')
	return render(request, 'courses/remove.html', {'application': application})
	
	
def add_lesson(request, pk):
	course = Course.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = LessonModelForm(request.POST)
		if model_form.is_valid():	
			model_form.save()
			name = model_form.cleaned_data['subject']
			messages.success(request, 'Lesson %s has been successfully added.' % (name))
			return redirect('courses:detail', course.id)
	else:
		model_form = LessonModelForm(initial={'course': pk})
	return render(request, 'courses/add_lesson.html', {'model_form': model_form})

