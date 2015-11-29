from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from coaches.models import Coach

def detail(request, coach_id):
	coach = get_object_or_404(Coach, pk=coach_id)
	context = {'coach' : coach}
	return render(request, './coaches/detail.html', context)


