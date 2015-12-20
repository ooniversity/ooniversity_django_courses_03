from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
import datetime
from courses.models import Course


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
'''
def handler404(request):
    response = render_to_response('errors/404.html', { 'message' : 'Sorry, page is not found' },
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('errors/500.html', { 'message' : 'Sorry, internal server error occurred' },
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
'''
'''
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html',
                  {'courses':courses,
                   })

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')
	
def student_detail(request):
	return render(request, 'student_detail.html')
'''

