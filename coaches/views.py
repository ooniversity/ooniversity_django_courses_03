from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    who_coach = []
    who_assistant = []
    for course in Course.objects.all():
        if coach == course.coach:
            who_coach.append(course)
        if coach == course.assistant:
            who_assistant.append(course)

    return render (request, 'coaches/detail.html', {'coach': coach, 'who_coach': who_coach, 'who_assistant': who_assistant})


