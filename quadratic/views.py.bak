# -*- coding: utf-8 -*- 
from django.shortcuts import render
from quadratic.forms import *

def get_quadratic (**kwargs):
    a, b, c = float(kwargs['a']), float(kwargs['b']), float(kwargs['c'])
    discr = b**2 - 4 * a * c;
    data = dict(d=int(discr))
    if discr < 0:
        data['d_mess'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif discr == 0:
        x = -b / (2 * a)
        data['d_mess'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
    else:
        x1 = (-b + discr ** (1/2.0)) / (2*a)
        x2 = (-b - discr ** (1/2.0)) / (2*a)
        data['d_mess'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)

    return data

def quadratic_results(request):
    form = QuadraticForm()
    if request.method == 'GET':
        rqst = request.GET
        form = QuadraticForm(rqst)
        if form.is_valid():
            context = get_quadratic(**form.cleaned_data)
            context['discr'] = True
        else:
            context = {k+'_err':'коэффициент не целое число' for k,v in rqst.items() if not v.strip('-').isdigit() and v != ''}
            context.update({k:rqst[k] for k in rqst.keys()})
    else:
        form = QuadraticForm()
    context['form'] = form
    return render(request, 'quadratic/results.html', context)
