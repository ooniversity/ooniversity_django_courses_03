from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
    coaches = Coach.objects.get(id=pk)
    context = {'coaches': coaches}

    coach_courses = Course.objects.filter(coach=pk)
    assistants_courses = Course.objects.filter(assistant=pk)
    context['coach_courses'] = coach_courses
    context['assistants_courses'] = assistants_courses
    return render(request, 'coaches/detail.html', context)
