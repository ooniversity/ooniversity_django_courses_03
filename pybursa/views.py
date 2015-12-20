from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
from polls.models import Choice, Question


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'data': 'some_data',
    })
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('contact.html')
    context = RequestContext(request, {
        'data': 'some_data',
    })
    return HttpResponse(template.render(context))

def student_list(request):
    template = loader.get_template('student_list.html')
    context = RequestContext(request, {
        'data': 'some_data',
    })
    return HttpResponse(template.render(context))

def student_detail(request):
    template = loader.get_template('student_detail.html')
    context = RequestContext(request, {
        'data': 'some_data',
    })
    return HttpResponse(template.render(context))

def page_not_found(request):
    return render(request,'404.html', status=404)

def server_error(request):
    return render(request,'500.html', status=500)
