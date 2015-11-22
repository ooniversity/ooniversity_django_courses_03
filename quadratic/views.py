# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.


def descriminant(request, a, b, c):
    return int(float(b)**2-4*float(a)*float(c))


def d_null(request, a, b):
    result = -float(b)/2*float(a)
    text = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % result
    return text


def double_result(request, a, b, d):
    a = float(a)
    b = float(b)
    x1 = (- b + d ** (1 / 2.0)) / 2 * a
    x2 = (- b - d ** (1 / 2.0)) / 2 * a
    text = u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (round(x1, 2), round(x2, 2))
    return text


def quadratic_results(request):
    flag_mistake = False
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    d_data = {'a': a, 'b': b, 'c': c}
    for i in d_data.keys():
        discription = 'mistake_%s' % i
        if d_data[i] == '':
            d_data[discription] = u'коэффициент не определен'
            flag_mistake = True
        elif not d_data[i].replace('-', '').isdigit():
            d_data[discription] = u'коэффициент не целое число'
            flag_mistake = True
        elif i == 'a' and not int(d_data[i]):
            d_data[discription] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            flag_mistake = True

    if not flag_mistake:
        d = descriminant(request, a, b, c)
        d_data['d'] = d
        if d < 0:
            d_data['mistake_d'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif not d:
            d_data['result'] = d_null(request, a, b)
        else:
            d_data['result'] = double_result(request, a, b, d)

    return render(request,'results.html', d_data)
