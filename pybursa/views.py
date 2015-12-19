from django.shortcuts import render, render_to_response
from django.template import RequestContext
from courses.models import Course


def index(request):
	return render(request, 'index.html', {'course': Course.objects.all()})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')
'''
def handler404(request):
    response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' },
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', { 'message' : 'Sorry, internal server error occurred' }, context_instance=RequestContext(request))
    response.status_code = 500
    return response
'''

