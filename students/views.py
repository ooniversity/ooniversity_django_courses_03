from django.shortcuts import render, redirect
from django.contrib import messages
from students.forms import StudentModelForm
from courses.models import Course
from students.models import Student
# Create your views here.

def list_view(request):
    if request.GET.get('course_id'):
    	course_id = request.GET.get('course_id')
    	students = Student.objects.filter(courses=course_id)
    	
    else:
    	students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})


def detail(request, id):
	student = Student.objects.get(id=id)
	return render(request, "students/detail.html", {"student": student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student_new = form.save()
            message = "Student %s %s has been successfully added."  %(student_new.name, student_new.surname)
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form': form})

def edit(request, id):
    student_edit = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student_edit)
        if form.is_valid():
            student_edit = form.save()
            message = "Info on the student has been sucessfully changed."
            messages.success(request, message)
            return redirect('students:edit', id)
    else:
    	form = StudentModelForm(instance=student_edit)
    return render(request, "students/edit.html", {'form': form})

def remove(request, id):
    student_del = Student.objects.get(id=id)
    if request.method == 'POST':
        student_del.delete()
        message =  "Info on %s %s has been sucessfully deleted." %(student_del.name, student_del.surname)
        messages.success(request, message)
        return redirect('students:list_view')
    return render(request, "students/remove.html", {"student_name": student_del.name, "student_surname": student_del.surname,})
