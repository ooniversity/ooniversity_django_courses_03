from django.shortcuts import render
import models
from coaches.models import Coach
from courses.models import Course


def detail(request, num):
    coacher=models.Coach.objects.get(id=num)
    coaches=Coach.objects.all()
    coach=Coach.objects.get(id=num)
    is_coach = [] 
    is_assist = []
    for i in Course.objects.all():
        if coach == i.coach:
            is_coach.append(i)
        if coach == i.assistant:
            is_assist.append(i)

    print is_coach
    print is_assist
    #print coacher__email
    

    return render(request, 'coaches/detail.html', {
        "coaches": coaches,
        "coacher": coacher,
        "is_coach": is_coach,
        "is_assist": is_assist,
        })

