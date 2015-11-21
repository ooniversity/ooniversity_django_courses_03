from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


def quadratic_results(request):
    print request.method
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    c = int(request.GET['c'])
    
    print a
    print b
    print c

    return render(request, 'results.html', {"a": a})

