# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    list_courses = Course.objects.all().order_by('name')
    context = {
        'list_courses': list_courses,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def page_not_found(request):
    response = render_to_response('404_v2.html', {'message': 'Sorry, page is not found'},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    response = render_to_response('500_v2.html', {'message': 'Sorry, internal server error occurred'},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
