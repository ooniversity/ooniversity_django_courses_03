from django.shortcuts import render
from students.models import Student
from courses.models import Course

	
def list_view(request):
	r = request.GET
	if 'course_id' in r:
		students = Student.objects.filter(courses=r['course_id'])
	else:
		students = Student.objects.all()
	return render(request, 'students/list.html', {'students': students})
	
def detail(request, pk):
	students = Student.objects.filter(id=pk)
	return render(request, 'students/detail.html', {'students': students})
