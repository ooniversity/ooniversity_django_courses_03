from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
from students.models import Student

def detail(request, teacher_id):
    teacher = get_object_or_404(Coach, pk=teacher_id)
    course_coach = Course.objects.filter(coach_id = teacher_id)
    course_assistant = Course.objects.filter(assistant_id = teacher_id)
    return render (request, 'coaches/detail.html',{'teacher':teacher,'course_coach':course_coach, 'course_assistant':course_assistant, })
