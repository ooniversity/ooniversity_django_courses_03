from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from students.forms import StudentModelForm
from students.models import Student


def list_view(request):
	try:
		id_course= request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
	return render(request,'students/list.html',{'name_stud': n_student})

def detail(request, id_student):
	n_student = Student.objects.filter(id=id_student)
	return render(request,'students/detail.html',{'name_student': n_student[0]})
	
def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			added_student = form.save()
			messages.success(request, 'Student %s %s has been successfully added' % (added_student.name, added_student.surname))
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {"form": form})

def edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', student_id = student.id)
	else:
		form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		student.delete()
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student': student})
	

