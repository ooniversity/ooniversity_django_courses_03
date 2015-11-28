from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson


def detail(request, course_id):
    #course = Course.objects.get(pk = course_id)
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course = course_id)
    return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})
