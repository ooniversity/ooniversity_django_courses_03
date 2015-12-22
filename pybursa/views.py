from django.shortcuts import get_object_or_404, render,  render_to_response
from courses.models import Course
from django.http import HttpResponse


def index(request):
	cour = Course.objects.all()
	return render(request, 'index.html', {'course': cour})


def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')

