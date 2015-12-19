from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question
from django.views import generic
from courses.models import Course
from django.template import RequestContext




def index(request):
	n_course = Course.objects.all()
	return render(request,'index.html',{'name_course': n_course})
	

def contact(request):
	return render(request,'contact.html')
	
def student_list(request):
	return render(request,'student_list.html')
	
def student_detail(request):
	return render(request,'student_detail.html')	
	
def page_not_found404(request):
	response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' }, 
								context_instance=RequestContext(request))
	response.status_code = 404
	return response

def internal_error500(request):
	response = render_to_response('500.html', context_instance=RequestContext(request))
	response.status_code = 500
	return response	
