#-*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    content = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            var_a = data['a']
            var_b = data['b']
            var_c = data['c']
            d = var_b**2 - 4*var_a*var_c
            content['d'] = d
            if d == 0:
                content['x1'] = round(float((-var_b + d ** (1/2.0))/ 2.0*var_a))
            elif d > 0:
                content['x1'] = round(float((-var_b + d ** (1/2.0))/ 2.0*var_a))
                content['x2'] = round(float((-var_b - d ** (1/2.0))/ 2.0*var_a))
            else:
                content['x1'] = ''
    else:
        form = QuadraticForm()
    content['form'] = form
    return render(request, "results.html", content)
