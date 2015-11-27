from django.shortcuts import render
from courses.models import Course

def index(request):
	courses_list = Course.objects.all()

	print courses_list

	context = {'courses_list' : courses_list}
	
	return render(request, './courses/index.html', context)

