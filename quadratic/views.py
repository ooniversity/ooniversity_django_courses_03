# -*- coding: utf-8 -*-
__author__ = 'dimon'
import math
from django.shortcuts import render_to_response


def quadratic_results(request):

    open_get = request.GET
    print(open_get)

    for key, value in open_get.items():
        if value.isdigit():
            print('It is digit ', value)
        if not value:
            value = 'коэффициент не определен'
            print(key, value)
        elif isinstance(value, str):
            value = 'коэффициент не целое число'
            print(key, value)

    # value = 'коэффициент не определен'
    # print(key + ' = ' + value)
    a = 1
    b = 1
    c = 1

    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        import math
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        context = {
            'title': 'Решение квадратного уравнения',
            'a': a,
            'b': b,
            'c': c,

        }
    elif discr == 0:
        x = -b / (2 * a)
        context = {
            'title': 'Решение квадратного уравнения',
            'a': a,
            'b': b,
            'c': c,

        }
    else:
        context = {
            'title': 'Решение квадратного уравнения',
            'a': a,
            'b': b,
            'c': c,

        }

    return render_to_response('results.html', context)
