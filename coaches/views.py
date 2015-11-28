from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, teacher_id):
	teacher = Coach.objects.get(id=teacher_id)
	course_where_coach = []	
	course_where_assistant = []
	for course in Course.objects.all():
		if teacher == course.coach:
			course_where_coach.append(course)
		if teacher == course.assistant:
			course_where_assistant.append(course)
	return render(request, 'coaches/detail.html', {'teacher':teacher, 'course_where_coach':course_where_coach, 'course_where_assistant':course_where_assistant})
