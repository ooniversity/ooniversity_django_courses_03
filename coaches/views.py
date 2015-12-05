from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist


def detail(request, detail_id):
	return render(request, 'coaches/detail.html', {'coach': Coach.objects.get(id = detail_id), 'course': Course.objects.filter(coach=detail_id), 'assist': Course.objects.filter(assistant=detail_id)})


def detail(request, pk):
	try:
		coach = Coach.objects.get(pk=pk)
		coach.full_name = coach.user.get_full_name()
		coach.email = coach.user.email
		coach.courses_coach = Course.objects.filter(coach=coach)
		coach.courses_assistant = Course.objects.filter(assistant=coach)
		return render(request, 'coaches/detail.html', {
	    	"coach": coach,
	    	})
	except ObjectDoesNotExist:
		message = "Sorry, no coach with id = {0} exist yet.".format(pk) 
		return render(request, 'coaches/detail.html', {
		    "message": message,
            })
