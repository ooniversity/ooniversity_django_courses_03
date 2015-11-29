# -*- coding:UTF-8 -*-
from django.shortcuts import render
from courses.models import Course, Lesson


def detail (request, course_id):
       details = Course.objects.get(id=course_id)
       lessons = Lesson.objects.filter(course=course_id)
       return render (request, 'courses/detail.html',  {'course_detail': details, 'lessons_list': lessons})