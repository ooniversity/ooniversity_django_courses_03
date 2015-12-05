from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from courses.models import Course, Lesson



def index(request):

    courses_list = Course.objects.all()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'courses_list': courses_list,
    })
    return HttpResponse(template.render(context))


def couse_detail(request, course_id):

    course = Course.objects.get(pk = course_id)
    lessons_list = Lesson.objects.filter(course = course)
    template = loader.get_template('courses/detail.html')
    context = RequestContext(request, {
        'course': course,
        'lessons_list': lessons_list
    })
    return HttpResponse(template.render(context))

