from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question
from django.views import generic
from courses.models import Course



def index(request):
	n_course = Course.objects.all()
	return render(request,'index.html',{'name_course': n_course})
	

def contact(request):
	return render(request,'contact.html')
	
def student_list(request):
	return render(request,'student_list.html')
	
def student_detail(request):
	return render(request,'student_detail.html')		
