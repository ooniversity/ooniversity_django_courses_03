# -*- coding:UTF-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    import math, cmath
    input_request = request.GET.dict()
    output_request = {}
    output_request['calculate'] = True

    try:
        output_request['a'] = int(input_request['a'])
    except:
        output_request['calculate'] = False
        output_request['a'] = input_request['a']
        if len(input_request.get('a')) == 0:
            output_request['a_error'] = "коэффициент не определен"
        elif not input_request['a'].isdigit():
            output_request['a_error'] = "коэффициент не целое число"
    finally:
        if input_request['a'].isdigit() and int(input_request['a']) == 0:
            output_request['calculate'] = False
            output_request['a_error'] = "коэффициент при первом слагаемом уравнения не может быть равным нулю" 

    try:
        output_request['b'] = int(input_request['b'])
    except:
        output_request['b'] = input_request['b']
        output_request['calculate'] = False
        if len(input_request.get('b')) == 0:
            output_request['b_error'] = "коэффициент не определен"
        elif not input_request['b'].isdigit():
            output_request['b_error'] = "коэффициент не целое число"

    try:
        output_request['c'] = int(input_request['c'])
    except:
        output_request['c'] = input_request['c']
        output_request['calculate'] = False
        if len(input_request.get('c')) == 0:
            output_request['c_error'] = "коэффициент не определен"
        elif not input_request['c'].isdigit():
            output_request['c_error'] = "коэффициент не целое число"  

    if output_request['calculate']:
        output_request['D'] = output_request['b']**2 - 4*output_request['a']*output_request['c']
        if output_request['D'] > 0:
            output_request['x1'] = float((-output_request['b'] + math.sqrt(output_request['D']))/(2*output_request['a']))
            output_request['x2'] = float((-output_request['b'] - math.sqrt(output_request['D']))/(2*output_request['a']))
        elif output_request['D'] == 0:
            output_request['x1'] = output_request['x2'] = float(-output_request['b'] / 2*output_request['a'])
        elif output_request['D'] < 0:
            output_request['x1'] = complex((-output_request['b'] + cmath.sqrt(output_request['D']))/(2*output_request['a']))
            output_request['x2'] = complex((-output_request['b'] - cmath.sqrt(output_request['D']))/(2*output_request['a']))    
    form01 = QuadraticForm()
    output_request['formq'] = form01
    print output_request
    return render(request,'quadratic/results.html',output_request)

