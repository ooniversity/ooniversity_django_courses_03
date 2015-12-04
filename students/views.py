# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentForm
from django.contrib import messages

	
def list_view(request):
	r = request.GET
	if 'course_id' in r:
		students = Student.objects.filter(courses=r['course_id'])
	else:
		students = Student.objects.all()
	return render(request, 'students/list.html', {'students': students})

	
def detail(request, pk):
	students = Student.objects.filter(id=pk)
	return render(request, 'students/detail.html', {'students': students})

	
def create(request):
	if request.method == 'POST':	
		model_form = StudentForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			name = model_form.cleaned_data['name']
			surname = model_form.cleaned_data['surname']
			messages.success(request, 'Student %s %s has been successfully added.' % (name, surname))
			return redirect('students:list_view')
	else:
		model_form = StudentForm()
	return render(request, 'students/add.html', {'model_form': model_form})


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = StudentForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', application.id)
	else:
		model_form = StudentForm(instance=application)
	return render(request, 'students/edit.html', {'model_form': model_form})
	

def remove(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()	
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'application': application})	
	
		
