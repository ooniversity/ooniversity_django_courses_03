# -*- coding: utf-8 -*
from django.shortcuts import render
from django.http import HttpResponse


def quadratic_results(request):
    print request.GET
    print request.GET['a']
    args = {}
    args['a'] = request.GET['a']
    try:
        args['a'] = int(request.GET['a'])
        if args['a'] == 0:
            args[
                'a_equal_zero'] = 'коэффициент при первом слагаемом не может быть равным нулю'
        else:
            a = args['a']
    except:
        a = 'none'
        if request.GET['a'] == '':
            args['a_empty'] = 'коэффициент не определен'
        else:

            args['a_not_int'] = 'коэффициент не целое число'

    args['b'] = request.GET['b']
    try:
        args['b'] = int(request.GET['b'])

        b = args['b']
    except:
        b = 'none'
        if request.GET['b'] == '':
            args['b_empty'] = 'коэффициент не определен'
        else:

            args['b_not_int'] = 'коэффициент не целое число'
    args['c'] = request.GET['c']
    try:
        args['c'] = int(request.GET['c'])

        c = args['c']
    except:
        c = 'none'
        if request.GET['c'] == '':
            args['c_empty'] = 'коэффициент не определен'
        else:

            args['c_not_int'] = 'коэффициент не целое число'

    try:
        d = b ** 2 - 4 * a * c

        args['d'] = 'Дискриминант: {}'.format(d)
        if d < 0:
            args['d_less_zero'] = 'Дискриминант менше нуля, квадратное уравнение не имеет действительных решений.'

        elif d == 0:
            x1 = x2 = -b / 2 * a
            args[
                'd_equal_zero'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(d)
        else:
            x1 = (-b + d ** (1 / 2.0)) / (2 * a)
            x2 = (-b - d ** (1 / 2.0)) / (2 * a)
            args['d_norm'] = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(
                x1, x2)
    except:
        pass

    return render(request, 'results.html', args)
