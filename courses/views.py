from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	context = {'course' : course}
	return render(request, './courses/detail.html', context)

def add(request):
	form = CourseModelForm() 
	if request.method == "POST":
	    form = CourseModelForm(request.POST)
	    if form.is_valid():
	    	data = form.cleaned_data
	    	form.save()
	    	msg = 'Course %s has been successfully added.' % (data['name'])
	    	messages.success(request, msg)
	    	return redirect('index')

	return render(request, 'courses/add.html', { 'form' : form })

def edit(request, course_id):
	course = Course.objects.get(id = course_id)
	form = CourseModelForm(instance=course) 

	if request.method == 'POST':
	    form = CourseModelForm(request.POST, instance=course)
	    if form.is_valid():
	    	form.save()
	    	data = form.cleaned_data
	    	msg = 'The changes have been saved.'
	    	messages.success(request, msg)
	    	redirect('courses:edit', course_id)

	return render(request, 'courses/edit.html', { 'form' : form } )

def remove(request, course_id):
	course = Course.objects.get(id = course_id)
	if request.method == "POST":
	    course.delete()
	    msg = 'Course %s has been deleted.' % course.name
	    messages.success(request, msg)
	    return redirect('index')

	return render(request, 'courses/remove.html', { 'course' : course })

#################
def add_lesson(request, course_id):
	course = Course.objects.get(id = course_id)
	form = LessonModelForm(initial={'course' : course})
	if request.method == "POST":
	    form = LessonModelForm(request.POST)
	    if form.is_valid():
			form.save()
			data = form.cleaned_data
			msg = 'Lesson %s has been successfully added.' % (data['subject'])
			messages.success(request, msg)
			return redirect('courses:detail', course.id)
	return render(request, 'courses/add_lesson.html', { 'form' : form })


