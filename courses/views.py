from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, id_course):
	id_c = '?course_id=' + id_course
	n_lesson = Lesson.objects.filter(course_id=id_course)
	course = Course.objects.get(id=id_course)
	return render(request,'courses/detail.html',{'name_lesson': n_lesson,'id_c':id_c, 'course':course})


