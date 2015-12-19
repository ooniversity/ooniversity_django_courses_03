from django.shortcuts import render, render_to_response
from courses.models import Course
from django.views.generic import TemplateView
from django.template import RequestContext

courses = Course.objects.all()
def index(request):
    return render(request, 'index.html', 
    	{'courses': courses})

class ContactView(TemplateView):
	template_name = "contact.html"

def custom_page_not_found(request):
	response = render_to_response('404.html', {'message' : 'Sorry, page is not found'},
                                  context_instance=RequestContext(request))
	response.status_code = 404
	return response

def custom_500_server_error(request):
	response = render_to_response('500.html', {'message' : 'Sorry, internal server error occurred'},
                                  context_instance=RequestContext(request))
	response.status_code = 500
	return response