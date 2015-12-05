from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from quadratic import quadratic_func

def quadratic(request):
    return render(request, 'quadratic.html')

def quadratic_results(request):
    data = {}
    data['a'] = request.GET['a']
    data['b'] = request.GET['b']
    data['c'] = request.GET['c']

    quadratic_func.quadratic_func(data)

    return render(request, 'results.html', {
        "data": data,
        })
