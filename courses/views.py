from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course_id = course_id)
    coach = Coach.objects.get(coach_courses = course_id)
    assistant = Coach.objects.get(assistant_courses = course_id)
    return render (request, 'courses/detail.html',{'course':course,'lessons':lessons, 'coach': coach, 'assistant':assistant})
