# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


def quadratic_start(request):
    return render(request, 'results_start.html')


def quadratic_results(request):

    lists_of_vars = {}

    lists_of_vars['a'] = str(request.GET['a'])
    lists_of_vars['b'] = str(request.GET['b'])
    lists_of_vars['c'] = str(request.GET['c'])

    for key, value in lists_of_vars.items():

        if key == 'a' and value == '0':
            lists_of_vars['a_msg'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        elif value == '':
            lists_of_vars[key+'_msg'] = 'коэффициент не определен'
        elif ''.join(x for x in value if x.isdigit()).isdigit() is False:
            lists_of_vars[key+'_msg'] = 'коэффициент не целое число'
        else:
            lists_of_vars[key+'_msg'] = 'ок'

    if lists_of_vars['a_msg'] is 'ок' and \
            lists_of_vars['b_msg'] is 'ок' and \
            lists_of_vars['c_msg'] is 'ок':

        a = float(lists_of_vars['a'])
        b = float(lists_of_vars['b'])
        c = float(lists_of_vars['c'])

        discr = b**2 - 4 * a * c;

        if discr > 0:
            import math
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            lists_of_vars['x1'] = round(x1, 1)
            lists_of_vars['x2'] = round(x2, 1)
        elif discr == 0:
            lists_of_vars['x'] = -b / (2 * a)
            
        if discr.is_integer():
            lists_of_vars['discr'] = int(discr)
        else:
            lists_of_vars['discr'] = discr

    return render(request, 'results.html', {
        "lists_of_vars": lists_of_vars,
        })

