from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
	return render(request, 'coaches/detail.html', 
				 {'coach': Coach.objects.get(id=pk), 
				  'course': Course.objects.filter(coach=pk),
				  'assistant': Course.objects.filter(assistant=pk)})