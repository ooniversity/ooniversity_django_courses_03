from django.shortcuts import render

from courses.models import Course


def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    lessons = courses.lesson_set.all()
    coaches = courses.coach.user.get_full_name()
    assistants = courses.assistant.user.get_full_name()
    return render(request,
                  'courses/detail.html', {
                      'courses': courses,
                      'lessons': lessons,
                      'coaches': coaches,
                      'assistants': assistants
                  })
