from django.shortcuts import render,get_object_or_404,redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages





def list_view(request):
	course_id = request.GET.get('course_id', None)
	context = {}

	if course_id is None:
		students = Student.objects.all()
		context = {'student_list' : students}
	else:
		students = Student.objects.filter(course__pk=course_id)
		context = {'student_list' : students}

	return render(request, './students/list.html', context)

def detail(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	context = {'student' : student}
	return render(request, './students/detail.html', context)

def create(request):
	if request.method == "POST":
	    form = StudentModelForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	data = form.cleaned_data
	    	msg = 'Student %s %s has been successfully added.' % (data['name'], data['surname'])
	    	messages.success(request, msg)
	    	return redirect('students:list_view')
	else:
		form = StudentModelForm() 

	return render(request, './students/add.html', { 'student_form' : form })

def edit(request, student_id):
	student = Student.objects.get(id = student_id)
	form = StudentModelForm(instance=student) 

	if request.method == 'POST':
	    form = StudentModelForm(request.POST, instance = student)
	    if form.is_valid():
	    	form.save()
	    	data = form.cleaned_data
	    	msg = 'Info on the student has been sucessfully changed.'
	    	messages.success(request, msg)

	return render(request, './students/edit.html', { 'form' : form } )

def remove(request, student_id):
	student = Student.objects.get(id = student_id)
	if request.method == "POST":
	    student.delete()
	    msg = 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname)
	    messages.success(request, msg)
	    return redirect('students:list_view')

	return render(request, './students/remove.html', { 'student' : student })



