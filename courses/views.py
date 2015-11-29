from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

# Create your views here.
def detail(request, course_id):
	course = Course.objects.get(id = course_id)
	lessons = Lesson.objects.filter(course = course_id)
	coach = course.coach.full_name()
	coach_descr = course.coach.description
	c = course.coach.id
	assistant = course.assistant.full_name()
	as_descr = course.assistant.description.
	a = course.assistant.id
	return render(request, 'courses/detail.html', 
		{'course':course, 'lessons':lessons, 'coach':coach, 'assistant':assistant, 'c':c, 'coach_descr':coach_descr, 'as_descr':as_descr})
