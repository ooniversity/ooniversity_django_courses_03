from django.shortcuts import render

from courses.models import Course, Lesson


def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course_id)
    return render(request,
                  'courses/detail.html', {'courses': courses, 'lessons': lessons})
