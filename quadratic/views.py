from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


def quadratic_results(request):
    print request.method
    #print request.GET['a']
    #print request.GET['b']
	
	#c = print request.GET['c']
	
	

    return render(request, 'results.html')

