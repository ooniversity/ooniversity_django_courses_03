from django.shortcuts import render, redirect
from courses.models import Course
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

# Create your views here.
def list_view(request):
	if request.GET.get('course_id'):
		course = Course.objects.get(id = request.GET.get('course_id'))
		students = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		students = Student.objects.all()
		course = Course.objects.all()
	return render(request, 'students/list.html', {'students':students})

def detail(request, student_id):
	student = Student.objects.get(id = student_id)
	return render(request, 'students/detail.html', {'student':student})

def create(request):
	form = StudentModelForm()
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			messages.success(request, 'Student %s %s has been successfully added.' % (name, surname))
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form':form})


def edit(request, student_id):
	student = Student.objects.get(id = student_id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance = student)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', student.id)
	else:
		form = StudentModelForm(instance = student)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, student_id):
	student = Student.objects.get(id = student_id)
	if request.method == 'POST':
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		student.delete()
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student':student})
