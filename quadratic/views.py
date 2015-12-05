# -*- coding:UTF-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    import math, cmath
    output_request = {}
    output_request['calculate'] = False
    if request.GET:
        tmp_form = QuadraticForm(request.GET)
        if tmp_form.is_valid():
            output_request['calculate'] = True
            a = tmp_form.cleaned_data['a']
            b = tmp_form.cleaned_data['b']
            c = tmp_form.cleaned_data['c']
            output_request['D'] = b**2 - 4*a*c
            if output_request['D'] > 0:
                output_request['x1'] = float((-b + math.sqrt(output_request['D']))/(2*a))
                output_request['x2'] = float((-b - math.sqrt(output_request['D']))/(2*a))
            elif output_request['D'] == 0:
                output_request['x1'] = output_request['x2'] = float(-b / 2*a)
            elif output_request['D'] < 0:
                output_request['x1'] = complex((-b + cmath.sqrt(output_request['D']))/(2*a))
                output_request['x2'] = complex((-b - cmath.sqrt(output_request['D']))/(2*a))    
    else:
        tmp_form = QuadraticForm()

    output_request['form'] = tmp_form
    return render(request,'quadratic/results.html',output_request)