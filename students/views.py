from django.shortcuts import render
from students.models import Student
from django.shortcuts import get_object_or_404, render
from courses.models import Course
from students.forms import StudentModelForm
from django.shortcuts import redirect
from django.contrib import messages


def list_view(request):
    try:
        a = request.GET.get('course_id')
        a = int(a)
        students_list = Student.objects.filter(courses=a)
    except:
        students_list = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': students_list})


def detail(request, pk):
    student_object =  get_object_or_404(Student, pk=pk) 
    return render(request, 'students/detail.html', {'student_object': student_object})


def create(request):
	if request.method == "POST":
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Student %s %s has been successfully added." % (student.name, student.surname))
			return redirect ('students:list_view')
		else:
			form = StudentModelForm(request.POST)
			return render(request, 'students/add.html', {'form':form})
	else:
		form = StudentModelForm()
		return render(request, 'students/add.html', {'form':form})


def edit(request, pk):
	student = Student.objects.get(pk=pk)
	if request.method == "POST":
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, "Info on the student has been sucessfully changed")
			return redirect ('students:list_view')
		else:
			form = StudentModelForm(request.POST, instance=student)
			return render(request, 'students/edit.html', {'form':form})
	else:
		form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, pk):
	student = Student.objects.get(pk=pk)
	if request.method == "POST":
		student.delete()
		messages.success(request, "Student %s %s has been successfully removed." % (student.name, student.surname))
		return redirect ('students:list_view')
	return render(request, 'students/remove.html', {'student': student})


	