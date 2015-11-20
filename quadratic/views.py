# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse


def quadratic_results(request):
    context = {}
    for key in request.GET.keys():
        try:
            context[key] = int(request.GET[key])
            context[key+'_status'] = 'int'
        except ValueError:
            if str(request.GET[key]):
                context[key] = str(request.GET[key])
            else:
                context[key] =''
            context[key+'_status'] = 'str'

    a = context['a']
    b = context['b']
    c = context['c']

    if all(map(lambda x: isinstance(x, int), (a, b, c))) and a != 0:
        context['dscrt'] = b**2 - 4*a*c
        if context['dscrt'] > 0:
            context['x1'] = float((-b + context['dscrt']**0.5) / (2 * a))
            context['x2'] = float((-b - context['dscrt']**0.5) / (2 * a))
        elif context['dscrt'] == 0:
            context['x1'] = context['x2'] = -b / (2 * a)
    else:
        context['dscrt'] = None

    return render(request, 'results.html', context)

