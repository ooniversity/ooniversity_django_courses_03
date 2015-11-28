from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

# Create your views here.
def detail(request, course_id):
	course = Course.objects.get(id = course_id)
	lessons = Lesson.objects.filter(course = course_id)
	coach = course.coach.full_name()
	c = course.coach.id
	assistant = course.assistant.full_name()
	return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons, 'coach':coach, 'assistant':assistant, 'c':c})
