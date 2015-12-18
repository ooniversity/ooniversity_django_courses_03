from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, master_id):
	master = Coach.objects.get(id=master_id)
	course_master = []	
	course_apprentice = []
	for course in Course.objects.all():
		if master == course.coach:
			course_master.append(course)
		if master == course.assistant:
			course_apprentice.append(course)
	return render(request, 'coaches/detail.html', {'master':master, 'course_master':course_master, 'course_apprentice':course_apprentice})
