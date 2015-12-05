from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson
from django.views import generic
from coaches.models import Coach
from django.contrib import messages
from courses.forms import CourseModelForm
from courses.forms import LessonModelForm
from django.shortcuts import redirect


def courses(request, id_course):
	id_c = '?course_id=' + id_course
	n_lesson = Lesson.objects.filter(course_id=id_course)
	course = Course.objects.get(id=id_course)
	return render(request,'courses/detail.html',{'name_lesson': n_lesson,'course': course, 'id_c':id_c})
	
def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			added_course = form.save()
			messages.success(request, 'Course %s has been successfully added.' % (added_course.name))
			return redirect('/')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {"form": form})
	
def edit(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=course)
		if form.is_valid():
			course = form.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit', course_id = course.id)
	else:
		form = CourseModelForm(instance=course)
	return render(request, 'courses/edit.html', {'form': form})
	
def remove(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == 'POST':
		course.delete()
		messages.success(request, 'Course %s has been deleted.' % (course.name))
		return redirect('/')
	return render(request, 'courses/remove.html', {'course': course})
	
def add_lesson(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form =LessonModelForm(request.POST)
        if form.is_valid():
            added_lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % added_lesson)
            return redirect('courses:detail', course_id=course.id)
    else:
        form = LessonModelForm(initial={'course': course})

    return render(request, 'courses/add_lesson.html', {"form": form})
	


