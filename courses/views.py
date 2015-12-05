from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    coach = Coach.objects.filter(coach_courses = course_id)
    assistant = Coach.objects.filter(assistant_courses = course_id)
    

    return render(request, 'courses/detail.html', { 'course': courses, 'coach': coach, 'assistant': assistant })
