from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, course_id):
    my_course = Course.objects.get(pk=course_id)
    my_lessons = Lesson.objects.filter(course=course_id)
    return render(request, "courses/detail.html", {'my_course': my_course, 'my_lessons': my_lessons})
