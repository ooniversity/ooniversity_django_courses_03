from django.shortcuts import render
from courses.models import Course

def index(request):
	courses_list = Course.objects.all()
	context = {'courses_list' : courses_list}
	return render(request, './index.html', context)
