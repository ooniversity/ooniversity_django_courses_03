# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
    output_dict = {}
    incoming_dict = request.GET.dict()
    output_dict['flag'] = True

    try:
        output_dict['a'] = int(incoming_dict['a'])
    except ValueError:
        output_dict['flag'] = False
        output_dict['a'] = incoming_dict['a']
        if len(incoming_dict.get('a')) == 0:
            output_dict['coef_a_err'] = u'коэффициент не определен'
        elif not incoming_dict['a'].isdigit():
            output_dict['coef_a_err'] = u'коэффициент не целое число'
    finally:
        if incoming_dict['a'].isdigit() and int(incoming_dict['a']) == 0:
            output_dict['flag'] = False
            output_dict['coef_a_err'] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю' 

    try:
        output_dict['b'] = int(incoming_dict['b'])
    except:
        output_dict['b'] = incoming_dict['b']
        output_dict['flag'] = False
        if len(incoming_dict.get('b')) == 0:
            output_dict['coef_b_err'] = u'коэффициент не определен'
        elif not incoming_dict['b'].isdigit():
            output_dict['coef_b_err'] = u'коэффициент не целое число'

    try:
        output_dict['c'] = int(incoming_dict['c'])
    except:
        output_dict['c'] = incoming_dict['c']
        output_dict['flag'] = False
        if len(incoming_dict.get('c')) == 0:
            output_dict['coef_c_err'] = u'коэффициент не определен'
        elif not incoming_dict['c'].isdigit():
            output_dict['coef_c_err'] = u'коэффициент не целое число'
    if output_dict['flag']:
    	output_dict['d'] = output_dict['b'] ** 2 - 4 * output_dict['a'] * output_dict['c']
    	if output_dict['d'] == 0:
    		output_dict['x'] = -output_dict['b'] / 2 * float(output_dict['a'])
    	elif output_dict['d'] > 0:
    		output_dict['x1'] = (-output_dict['b'] + output_dict['d'] ** (1/2.0)) / (2*output_dict['a'])
    		output_dict['x2'] = (-output_dict['b'] - output_dict['d'] ** (1/2.0)) / (2*output_dict['a'])	
 

    return render(request, 'quadratic/results.html', output_dict)
