from django.shortcuts import render, get_object_or_404
from coaches.models import Coach

from courses.models import Course

def detail(request, coach_id):
	coaches = get_object_or_404(Coach, pk = coach_id)
	courses = Course.objects.filter(coach = coach_id)
	assistants = Course.objects.filter(assistant = coach_id)
	return render(request, 'coaches/detail.html', {'coaches': coaches, 'courses': courses, 'assistants': assistants})