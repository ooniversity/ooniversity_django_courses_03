# -*- coding:UTF-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from courses.models import Course
# from students.models import Student
# from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})


def contact(request):
    return render(request, 'contact.html')


'''
def contact(request):
   return render(request, 'contact.html')

# implemented short record in urls.py

class ContactView(TemplateView):
   template_name = 'contact.html'


def list_view(request):
    return render(request, 'list.html', {'students': Student.objects.all()})

def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
'''

#
# def not_found(request):
#     response = render_to_response('errors/404.html', {'error_text': 'Sorry, page is not found'},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
#
#
# def server_error(request):
#     response = render_to_response('errors/500.html', {'error_text': 'Sorry, internal server error occurred'},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response

def not_found(request):
    response = render_to_response('404.html', {'error_text': 'Sorry, page is not found'},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    response = render_to_response('500.html', {'error_text': 'Sorry, internal server error occurred'},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
