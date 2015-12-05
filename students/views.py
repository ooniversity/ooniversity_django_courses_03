from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student
from courses.models import Course, Lesson
from django.contrib import messages
from students.forms import StudentModelForm

def list_view(request):
    if request.GET.get('course_id'):
        students = Student.objects.filter(courses = request.GET.get('course_id'))
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def detail(request,student_id):
    students = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(student__id= student_id)
    return render (request, 'students/detail.html', {'courses':courses,'students': students})

def add(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
			messages.success(request, message)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Info on the student has been sucessfully changed.')
	else:
		form = StudentModelForm(instance=application)
	return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		message = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
		messages.success(request, message)
		return redirect('students:list_view')
    return render(request, 'students/remove.html', {'full_name': application.name+ ' ' +application.surname})