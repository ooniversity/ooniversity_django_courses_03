from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course


def index(request):
    course = Course.objects.all()
    return render(request, 'index.html', {'courses': course })

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')


def error_404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

def error_500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response


