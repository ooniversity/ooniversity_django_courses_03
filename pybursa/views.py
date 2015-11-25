from django.shortcuts import render
from courses.models import Course

def index_courses(request):
	return render(request, 'index_courses.html', {'courses':Course.objects.all()})

def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')


