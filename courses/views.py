from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
def detail(request, course_id):
    courses = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.all()
    coaches = Coach.objects.all()

    return render (request, 'courses/detail.html',{'courses':courses,'lessons':lessons, 'coaches': coaches})