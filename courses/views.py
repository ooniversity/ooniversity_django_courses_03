from django.shortcuts import render
from courses.models import Course, Lesson

def course (request, course_id):
    course_id = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    return render(request, 'about_course.html', {'course': course_id, 'lesson': lessons})

# Create your views here.
