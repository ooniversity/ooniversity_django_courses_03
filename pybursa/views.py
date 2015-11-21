#from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader
#from django.http import Http404
#from django.views import generic
#from polls.models import Choice, Question


def index(request):
    #return HttpResponse("Hello, it is index.")
    return render(request, 'index.html')

def contact(request):
    #return HttpResponse("Hello, it is contact")
    return render(request, 'contact.html')

def student_list(request):
    #return HttpResponse("Hello, student_list")
    return render(request, 'student_list.html')

def student_detail(request):
    #return HttpResponse("Hello, student_detail")
    return render(request, 'student_detail.html')