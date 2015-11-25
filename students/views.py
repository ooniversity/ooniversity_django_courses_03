# -*- coding: utf-8 -*-
from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
	#if course_id is None:
	try:
		course_id = request.GET.get('course_id')
	#print(course_id)
		course = Course.objects.get(id=course_id)
		std = Student.objects.all()
		students = []
		for people in std:
			if course in people.courses.all():
				students.append(people)
		return render(request, 'students/list.html', {'students':students})
	except:
		students = Student.objects.all()
		return render(request, 'students/list.html', {'students':students})
def detail(request, student_id):
	student = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'student':student})
