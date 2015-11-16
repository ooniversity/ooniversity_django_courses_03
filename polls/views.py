from django.shortcuts import render
from polls.models import Poll

def instructors_list(request):
	polls = Poll.objects.all()
	return render(
		request, 'instructors_list.html', 
		{'polls': polls}
	)