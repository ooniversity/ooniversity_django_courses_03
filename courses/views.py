# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, course_id):
    #return HttpResponse('course_id = {}'.format(course_id))
    args = {}
            
    course = Course.objects.get(id=course_id)
    args['name'] = course.name
    args['description'] = course.description
    args['lesson1'] = Lesson.objects.filter(course__id=course_id)
    args['course_id'] = course_id
    #args['xuy'] = 'http://127.0.0.1:8000/students/?course_id={}'.format(course_id)
    args['coach_name'] = course.coach.name
    args['coach_surname'] = course.coach.surname
    args['coach_description'] = course.coach.description
    args['assistant_name'] = course.assistant.name
    args['assistant_surname'] = course.assistant.surname
    args['assistant_description'] = course.assistant.description
    args['coach'] = course.coach
    args['assistant'] = course.assistant


    #course.coach.coach_courses.select_related('coach_courses') - курсы тренера


    return render(request, 'courses/detail.html', args)
