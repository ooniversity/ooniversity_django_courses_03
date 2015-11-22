# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


def quadratic_start(request):
    return render(request, 'results_start.html')


def quadratic_results(request):




    def check_on_error(variable, zr_check=""):
        variable = ''.join(x for x in variable if x.isdigit())
        if variable == '0' and zr_check == 'a':
            return "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        elif variable == '':
            return "коэффициент не определен"
        elif variable.isdigit() is False:
            return "коэффициент не целое число"        
        else:
            return "absolute of %s is ok" % variable



    def quadr_riv(a,b,c):
        outpt_str = {}

        if a == '0':
            pass


        discr = b**2 - 4 * a * c;
        
        if discr > 0:
            import math
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
        elif discr == 0:
            x = -b / (2 * a)
            
        else:
            print("123")

        outpt_str['x1']=x1
        outpt_str['x2']=x2
        outpt_str['discr']=discr
        return outpt_str

    list1 = quadr_riv(int(request.GET['a']),
                int(request.GET['b']),
                int(request.GET['c']))

    print list1
    print list1['discr']

    a = str(request.GET['a'])
    b = str(request.GET['b'])
    c = str(request.GET['c'])




    return render(request, 'results.html', {
        "a": a,
        "b": b,
        "c": c,
        "check_on_error_a": check_on_error(a, "a"),
        "check_on_error_b": check_on_error(b),
        "check_on_error_c": check_on_error(c),
        "discr": list1['discr'],
        })



