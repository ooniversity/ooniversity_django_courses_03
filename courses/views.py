from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, num):
    item = Course.objects.get(id=num)
    lesson = Lesson.objects.filter(course=Course.objects.filter(id=num))
    coaches = Coach.objects.filter(coach_courses=num)
    assistants = Coach.objects.filter(assistant_courses=num)
    return render(request, 'courses\detail.html', {'item': item, 'lesson': lesson,
                                                   'coaches': coaches, 'assistants': assistants
                                                   }
                  )
