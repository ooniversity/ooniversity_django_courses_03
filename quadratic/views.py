# -*- coding: utf-8 -*-
__author__ = 'dimon'
import math
from django.shortcuts import render_to_response


def quadrato(a, b, c):
    pass


def quadratic_results(request):
    all_keys = request.GET.keys()

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    c = int(request.GET['c'])

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
