# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from coaches.models import Coach
from courses.models import Course


def detail(request, coache_id):
    coach = get_object_or_404(Coach, pk=coache_id)
    coach_on_courses = Course.objects.filter(coach=coache_id)
    assistant_on_courses = Course.objects.filter(assistant=coache_id)
    context = {
        'coach': coach,
        'coach_on_courses': coach_on_courses,
        'assistant_on_courses': assistant_on_courses,
    }
    return render(request, 'coaches/detail.html', context)
