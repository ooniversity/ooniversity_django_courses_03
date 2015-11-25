# -*- coding: utf-8 -*- 
from django.shortcuts import render
from students.models import Student
from courses.models import Course, Lesson
from django.http import HttpResponse

def list_view(request):
	if request.GET.get('course_id'):
		stud = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		stud = Student.objects.all()
	#print Student.courses.all()
	#lesn = Lesson.objects.filter(course=course_id)
	return render(request, 'students/list.html', {'students': stud})

def detail(request, detail_id):
	#stud = Student.objects.get(id = detail_id)
	
	#cour = Course.objects.get(id=course_id)
	#lesn = Lesson.objects.filter(course=course_id)
	return render(request, 'students/detail.html', {'student': Student.objects.get(id = detail_id)})



