from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
# Create your views here.
def list_view(request):
	if request.GET != {}:
		course_id = request.GET['course_id']
		student = Student.objects.filter(courses = course_id)
	else:
		student = Student.objects.all()

	return render(request, 'students/list.html', {'student':student})

def detail(request, student_id):
	student = Student.objects.get(pk=student_id)	
	return render(request, 'students/detail.html', {'student':student})

def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			message_string = "Student %s has been successfully added." % student.fullname()
			messages.success(request, message_string)
		return redirect('students:list_view')
	form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return render(request, 'students/edit.html', {'form': form})

    form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Info on %s has been sucessfully deleted." % student.fullname())
        return redirect('students:list_view')

    return render(request, 'students/remove.html', {'student': student})