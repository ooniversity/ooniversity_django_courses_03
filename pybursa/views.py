from django.shortcuts import render, render_to_response
from courses.models import Course
from django.template import RequestContext

def index(request):
    all_courses = Course.objects.all()
    return render(request, "index.html", {'all_courses': all_courses})

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")

def page_not_found_custom(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def page_error_found_custom(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
