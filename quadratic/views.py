# -*- coding:UTF-8 -*-

from django.shortcuts import render
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    params = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b * b - 4 * a * c
            if d < 0:
                params['d'] = d
            elif d == 0:
                x = (-b + d ** (1 / 2.0)) / 2 * a
                params['x1'] = round(x, 1)
                params['d'] = d
            else:
                x1 = (-b + d ** (1 / 2.0)) / 2 * a
                x2 = (-b - d ** (1 / 2.0)) / 2 * a
                params['x1'] = round(x1, 1)
                params['x2'] = round(x2, 1)
                params['d'] = d
    else:
        params['form'] = QuadraticForm()
    return render(request, 'quadratic/results.html', params)
