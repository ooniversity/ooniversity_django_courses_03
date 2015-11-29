from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
# Create your views here.
def detail(request, coach_id):
	coach = Coach.objects.get(pk=coach_id)	
	iamcoach = []
	iamassistant = []
	for eachcourse in Course.objects.all():
		if coach == eachcourse.coach:
			iamcoach.append(eachcourse)
		if coach == eachcourse.assistant:
			iamassistant.append(eachcourse) 
	return render(request, 'coaches/detail.html', {'coach':coach, 'iamcoach':iamcoach, 'iamassistant':iamassistant})