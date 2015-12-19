from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from courses.models import Course
from django.views.generic import TemplateView
from django.template import RequestContext


def page_not_found(request):
    response = render_to_response(
        '404.html', {'error_message': 'Sorry, page is not found'},
        context_instance=RequestContext(request)
        )

    response.status_code = 404

    return response

def server_error(request):
    response = render_to_response(
        '500.html', {'error_message': 'Sorry, internal server error occurred'},
        context_instance=RequestContext(request)
        )

    response.status_code = 500

    return response

class IndexView(TemplateView):
  template_name = 'index.html'
  
  def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

def index(request):
    args={}
    args['courses'] = Course.objects.all()

    return render(request, 'index.html', args)
def contact(request):
    return render(request, 'contact.html')
def student_list(request):
    return render(request, 'student_list.html')
def student_detail(request):
    return render(request, 'student_detail.html')            
    