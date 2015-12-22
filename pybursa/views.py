from django.shortcuts import get_object_or_404, render,  render_to_response
from courses.models import Course
from django.http import HttpResponse


def index(request):
	cour = Course.objects.all()
	return render(request, 'index.html', {'course': cour})


def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')

def not_found(request):
    response = render_to_response('errors/404.html', { 'message' : 'Sorry, page is not found' },
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    response = render_to_response('errors/500.html', { 'message' : 'Sorry, internal server error occurred' },
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response