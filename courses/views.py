from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	context = {'course' : course}
	return render(request, './courses/detail.html', context)

def add(request):
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Course %s has been successfully added.' % (data['name']))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', { 'form' : form })

def edit(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.POST:
	    form = CourseModelForm(request.POST, instance=course)
	    if form.is_valid():
	        form.save()
	        messages.success(request, 'The changes have been saved.')
	        return redirect('courses:edit',  course_id)
	else:
	    form = CourseModelForm(instance=course)
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
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % ( form.cleaned_data['subject']))
            return redirect('courses:detail', form.cleaned_data['course'].id)
    else:
        form = LessonModelForm(initial={ 'course' : course_id })
    return render(request, 'courses/add_lesson.html', { 'form' : form })

