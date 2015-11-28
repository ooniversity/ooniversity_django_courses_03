from django.shortcuts import render,get_object_or_404
from students.models import Student

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
