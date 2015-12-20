# -*- coding:UTF-8 -*-

from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coaches/detail.html', {'coach': coach, 'course_coach': Course.objects.filter(coach=coach),
                                                   'course_assistant': Course.objects.filter(assistant=coach)})
