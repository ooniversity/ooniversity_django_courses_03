from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
	course = Course.objects.get(pk=course_id)
	lesson = Lesson.objects.all()
	return render(request, 'courses/detail.html', {'course':course, "lesson": lesson})

