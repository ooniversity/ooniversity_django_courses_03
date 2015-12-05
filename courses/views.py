from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from courses.forms import CourseModelForm
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
			form.save()
			data = form.cleaned_data
			msg = 'Course %s has been successfully added.' % (data['name'])
			messages.success(request, msg)
			return redirect('/')

	return render(request, './courses/add.html', { 'form' : form })

def edit(request, course_id):
	course = Course.objects.get(id = course_id)
	form = CourseModelForm(instance=course) 

	if request.method == 'POST':
	    form = CourseModelForm(request.POST, instance=course)
	    if form.is_valid():
	    	form.save()
	    	data = form.cleaned_data
	    	msg = 'Info on the student has been sucessfully changed.'
	    	messages.success(request, msg)

	return render(request, './courses/edit.html', { 'form' : form } )

def remove(request, course_id):
	course = Course.objects.get(id = course_id)
	if request.method == "POST":
	    course.delete()
	    msg = 'Info on %s has been sucessfully deleted.' % course.name
	    messages.success(request, msg)
	    return redirect('/')

	return render(request, './courses/remove.html', { 'course' : course })

#################
def add_lesson(request):
	form = LessonModelForm() 
	if request.method == "POST":
	    form = LessonModelForm(request.POST)
	    if form.is_valid():
			form.save()
			data = form.cleaned_data
			msg = 'Lesson %s has been successfully added.' % (data['lesson_name'])
			messages.success(request, msg)
			return redirect(request, '/')
	return render(request, './courses/add_lesson.html', { 'form' : form })


