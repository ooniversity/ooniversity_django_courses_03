from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from quadratic import quadratic_func
from django import forms
from forms import QuadraticForm


def quadratic_start(request):
    return render(request, 'results_start.html')

def quadratic_results(request):
    context={}
    print type(context)
    form = QuadraticForm()
    context['form'] = form

    #print request.POST
    #print form
    #lists_of_vars['a'] = str(request.GET['a'])
    #lists_of_vars['b'] = str(request.GET['b'])
    #lists_of_vars['c'] = str(request.GET['c'])

    #quadratic_func.quadratic_func(lists_of_vars)

    return render(request, 'results.html', context)
