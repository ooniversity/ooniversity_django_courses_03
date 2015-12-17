# -*- coding:UTF-8 -*-
from django.shortcuts import render
from courses.models import Coach, Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    coach_object = Course.objects.filter(coach=coach_id)
    assistant_object = Course.objects.filter(assistant=coach_id)
    return render(request, 'coaches/detail.html', {'coach_detail': coach, 'teacher_in': coach_object, 'assistant_in': assistant_object})
