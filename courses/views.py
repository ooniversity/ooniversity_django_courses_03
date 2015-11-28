# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404

from .models import Course


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
    }
    return render_to_response('courses/detail.html', context)
