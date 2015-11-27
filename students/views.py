from django.shortcuts import render
from courses.models import Course
from students.models import Student

# Create your views here.
def students(request):
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