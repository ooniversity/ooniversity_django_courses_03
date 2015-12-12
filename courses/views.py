from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach

def course (request, course_id):
    course_id = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)

    coaches = Coach.objects.all()
    return render(request, 'about_course.html', {'course': course_id, 'lesson': lessons, 'coaches': coaches })

# Create your views here.
