# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course, Lesson, Coach

def detail(request, course_id):
    courses = Course.objects.get(id=course_id)

    return render(request, 'courses/detail.html', { 'course': courses,
                                                    'coach': courses.coach.user.get_full_name(),
                                                    'assistant': courses.assistant.user.get_full_name(),
                                                                                                    })
