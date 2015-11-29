from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from quadratic import quadratic_func

def quadratic_start(request):
    return render(request, 'results_start.html')

def quadratic_results(request):
    lists_of_vars = {}
    lists_of_vars['a'] = str(request.GET['a'])
    lists_of_vars['b'] = str(request.GET['b'])
    lists_of_vars['c'] = str(request.GET['c'])

    quadratic_func.quadratic_func(lists_of_vars)

    return render(request, 'results.html', {
        "params": lists_of_vars,
        })