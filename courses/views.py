from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
  course = Course.objects.get(id=course_id)
  lessons = Lesson.objects.all()
  topics = []
  for les in lessons:
    if les.course == course:
      topics.append(les)
  return render(request, 'courses/detail.html', {'course':course, 'lessons':topics})
