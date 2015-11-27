from django.shortcuts import render
from django.http import HttpResponse
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