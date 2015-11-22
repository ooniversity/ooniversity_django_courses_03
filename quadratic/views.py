# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


def quadratic_start(request):
    return render(request, 'results_start.html')


def quadratic_results(request):
    


    def is_int_err_1(data):



        print type(data)
        if type(data) is not int or type(data) is not float:
            data = "коэффициент не определен"
            return data
        else:
            return None
    def is_def_err_2(data):
        if data is None:
            return "коэффициент не целое число"
        else:
            return None


    a = float(request.GET['a'])
    b = float(request.GET['b'])
    c = float(request.GET['c'])

    a_err_1 = is_int_err_1(a)
    a_err_2 = is_def_err_2(a)

    x = x1 = x2 = 0


    discr = b**2 - 4 * a * c;
    print discr
    if discr > 0:
        import math
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
    elif discr == 0:
        x = -b / (2 * a)
    else:
        print("Корней нет")


    return render(request, 'results.html', {
        "a": a,
        "b": b,
        "c": c,
        "discr": discr,
        #"x": x,
        "x1": x1,
        "x2": x2,
        "a_err_1": a_err_1,
        "a_err_2": a_err_2,
        "is_int_err_1": is_int_err_1(a),
        })



