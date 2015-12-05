from django.shortcuts import render,redirect
from students.models import Student
from students.forms import StudentModelForm
from courses.models import Course
from django.contrib import messages

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


def edit(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == 'POST': 
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			#print 
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.' )
			return redirect('students:edit', pk = student.id)
	else:
		form = StudentModelForm(instance=student)	
	return render(request,'students/edit.html', {'form' : form})	


def remove(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == 'POST':
		student.delete()
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		return redirect('students:list_view')

	return render(request, 'students/remove.html', {'student': student})


def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			student = form.save()
			messages.success(request, 'Student ' + data['name'] + " " + data['surname'] + ' has been successfully added.' )
			return redirect('students:list_view')
	else:
		form = StudentModelForm()		
	return render(request,'students/add.html', {'form' : form})	
