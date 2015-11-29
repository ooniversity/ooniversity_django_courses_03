# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from coaches.models import Coach
from .models import Course
from django.core.exceptions import ObjectDoesNotExist


def detail(request, course_id):
    try:
        coach = Coach.objects.get(coach_courses__exact=course_id)
        assistant = Coach.objects.get(assistant_courses__exact=course_id)
    except ObjectDoesNotExist:
        coach = False
        assistant = False
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
        'coach': coach,
        'assistant': assistant,

    }
    return render_to_response('courses/detail.html', context)
