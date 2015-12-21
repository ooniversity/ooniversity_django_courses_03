from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach

def index(request):
	courses = Course.objects.all()
	coaches = Coach.objects.all()
	return render(request, 'index.html', {"courses": courses, 'coaches':coaches})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')
