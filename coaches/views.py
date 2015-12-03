from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

# Create your views here.
def detail(request, coach_id):
	coaches = Coach.objects.all()
	coach = Coach.objects.get(id = coach_id)
	course_coach = Course.objects.filter(coach_id = coach_id)
	course_assistant = Course.objects.filter(assistant_id = coach_id)
	return render(request, 'coaches/detail.html', {'coaches':coaches, 'coach':coach, 'course_coach':course_coach, 'course_assistant':course_assistant})