from django.shortcuts import render
from students.models import Student

def list_view(request):
	if request.GET.get('course_id'):
		students = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		students = Student.objects.all()
	return render(request, 'students/list.html', {'students': students})

def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})