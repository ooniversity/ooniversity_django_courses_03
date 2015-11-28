from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student
# Create your views here.
def list_view(request):
	if request.GET != {}:
		course_id = request.GET['course_id']
		student = Student.objects.filter(courses = course_id)
	else:
		student = Student.objects.all()

	return render(request, 'students/list_view.html', {'student':student})

def detail(request, student_id):
	student = Student.objects.get(pk=student_id)	
	return render(request, 'students/detail.html', {'student':student})