from django.shortcuts import render, render_to_response
from django.template import RequestContext
from courses.models import Course


def index(request):
    gcourses = Course.objects.all()
    return render(request,'index.html', {'gc': gcourses})

def contact(request):
    return render(request,'contact.html')

def student_list(request):
    return render(request,'student_list.html')

def student_detail(request):
    return render(request,'student_detail.html')

def page_not_found(request):
    response = render_to_response('status/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def server_error(request):
    response = render_to_response('status/500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


