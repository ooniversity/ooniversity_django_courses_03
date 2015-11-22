#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import math



def quadratic_results(request):
    result = {'a' : [request.GET['a'], ''],
               'b' : [request.GET['b'], ''],
               'c' : [request.GET['c'], '']
                }

    for item in result:
        if result[item][0] == '':
            result[item][1] = 'коэффициент не определен'
        else:
            try:
                int(result[item][0])
            except Exception:
                result[item][1] = 'коэффициент не целое число'
                continue
            if item == 'a' and int(result['a'][0]) == 0:
                result['a'][1] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if ''.join([result[item][1] for item in result]) == '':
        a = float(result['a'][0])
        b = float(result['b'][0])
        c = float(result['c'][0])
        d = (b*b)-(4*a*c)
        if d>0:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            d_help = 'Дискриминант: %.0f' % d
            help = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
            discr = {'d' : [d_help,help]}
        elif d==0:
            x = -float(b)/(2*float(a))
            d_help = 'Дискриминант: 0'
            help = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
            discr = {'d' : [d_help,help]}
        else:
            d_help = 'Дискриминант: %.0f' % d
            help = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            discr = {'d' : [d_help,help]}
        result.update(discr)

    return render(request, 'results.html', result)

