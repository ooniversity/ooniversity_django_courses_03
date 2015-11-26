from django.shortcuts import render
from courses.models import Course, Lesson
from django.http import HttpResponse

def detail(request, pk):
	return render(request, 'courses/detail.html', {'course': Course.objects.get(id = pk)})