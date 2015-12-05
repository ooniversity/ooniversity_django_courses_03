from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
	course = Course.objects.get(id=course_id)
	lessons = course.lesson_set.all()
	return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})

def create(request):
	if request.method == "POST":
		form = CourseModelForm(request.POST)
		if form.is_valid():
			cour = form.save()
			mes = u'Course %s has been successfully added.' % cour.name
			messages.success(request, mes)
			return redirect("/")
	else:
		form = CourseModelForm()
	return render(request, "courses/add.html", {'form':form})

def edit(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		form = CourseModelForm(request.POST, instance=course)
		if form.is_valid():
			cour = form.save()
			mes = u'The changes have been saved.'
			messages.success(request, mes)
			return redirect('courses:edit',  cour.id)
	else:
		form = CourseModelForm(instance=course)
	return render(request, "courses/edit.html", {'form':form})
	
def remove(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		course.delete()
		mes = u'Course %s has been deleted.' % course.name
		messages.success(request, mes)
		return redirect("/")

	return render(request, "courses/remove.html", {'name':course.name})
	
def add_lesson(request, course_id):
	if request.method == "POST":
		form = LessonModelForm(request.POST)
		if form.is_valid():
			les = form.save()
			mes = u'Lesson %s has been successfully added.' % les.subject
			messages.success(request, mes)
			return redirect('courses:detail', les.course.id)
	else:
		form = LessonModelForm()
	return render(request, "courses/add_lesson.html", {'form':form})

