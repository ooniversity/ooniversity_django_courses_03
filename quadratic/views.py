# -*- coding: utf-8 -*-
from django.shortcuts import render
import math


def replacer(dictionary):
    for item in dictionary.keys():
        if not dictionary[item]:
            dictionary[item] = 'коэффициент не определен'
        elif dictionary[item].isdigit():
            dictionary[item] = ''
        else:
            dictionary[item] = 'коэффициент не целое число'
    return dictionary


def quadratic_calc(a=None, b=None, c=None):
    errors = {'a': '', 'b': '', 'c': ''}
    get_dict = lambda: {'a': a, 'b': b, 'c': c, 'd': d, 'x1': x1, 'x2': x2, 'result': result, 'errors': errors}

    try:
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        x1, x2, d = None, None, None
        result = None
        errors = replacer({'a': a, 'b': b, 'c': c})
        return get_dict()

    try:
        d = round((math.pow(b, 2) - 4 * a * c), 2)

        if d > 0:
            x1 = round(((-b + math.sqrt(d)) / (2.0 * a)), 2)
            x2 = round(((-b - math.sqrt(d)) / (2.0 * a)), 2)
            result = [
                'Дискриминант: {0}'.format(d),
                'Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}'.format(x1, x2),
            ]
        elif d == 0:
            x1 = x2 = round((-b / (2.0 * a)), 2)
            result = [
                'Дискриминант: {0}'.format(d),
                'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}'.format(
                    x1),
            ]
        elif d < 0:
            x1, x2 = None, None
            result = [
                'Дискриминант: {0}'.format(d),
                'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.',
            ]

    except ZeroDivisionError:
        errors = {'a': 'коэффициент при первом слагаемом уравнения не может быть равным нулю', 'b': '', 'c': ''}
        x1, x2, d = None, None, None
        result = None

    return get_dict()


def quadratic_results(request):
    result = quadratic_calc(request.GET['a'], request.GET['b'], request.GET['c'])
    return render(request, 'results.html', {'result': result})


def equation(request):
    return render(request, 'equation.html')
