# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def get_dict_from_request (tpl, rqst):

    data = {k+'_err':'коэффициент не целое число' for k,v in rqst.items() if not v.strip('-').isdigit()}
    data.update({k:rqst[k] if k in rqst else '' for k in tpl})
    data.update({k+'_err': 'коэффициент не определен' for k in tpl if data[k] == ''})
    data.update({k+'_err': False for k in tpl if k+'_err' not in data})    
    data['a_err'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю' if data['a'] == '0' else data['a_err']
    return data

def get_quadratic (tpl):
    a, b, c = tpl
    data = {}
    a = float(a)
    b = float(b)
    c = float(c)
    d = discr = b**2 - 4 * a * c;
    data['d'] = int(d)
    if d < 0:
        data['d_mess'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif d == 0:
        x = -b / (2 * a)
        data['d_mess'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
    else:
        x1 = (-b + d ** (1/2.0)) / (2*a)
        x2 = (-b - d ** (1/2.0)) / (2*a)
        data['d_mess'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)

    return data

def quadratic_results(request):
    d, keys = True, ('a','b','c')
    data = get_dict_from_request (keys, request.GET)
    for item in keys:
        if data[item +'_err']:
            d = False
            break
    if d:
        data.update(get_quadratic ((data['a'], data['b'], data['c'])))
        data['discr'] = True
    else:
        data['discr'] = False
    return render_to_response('quadratic/results.html', data)
