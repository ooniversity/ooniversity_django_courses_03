# -*- coding: utf-8 -*-
__author__ = 'dimon'
import math
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    open_get = request.GET
    context = {
        'title': 'Quadratic Equation'
    }
    if request.method == "GET":
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            for key, value in open_get.items():
                if value:
                    if value[0] != '-':
                        if not value.isdigit():
                            context[key] = value
                            context['error' + '_' + key] = 'коэффициент не целое число'
                        else:
                            context[key] = int(value)
                    else:
                        if not value[1:].isdigit():
                            context[key] = value
                            context['error' + '_' + key] = 'коэффициент не целое число'
                        else:
                            context[key] = int(value)
                else:
                    context[key] = value
                    context['error' + '_' + key] = 'коэффициент не определен'
            if isinstance(context['a'], int) and isinstance(context['b'], int) and isinstance(context['c'], int):
                if context['a'] == 0:
                    context['error_a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                else:
                    discr = context['b'] ** 2 - 4 * context['a'] * context['c']
                    if discr > 0:
                        x1 = (-context['b'] + math.sqrt(discr)) / (2 * context['a'])
                        x2 = (-context['b'] - math.sqrt(discr)) / (2 * context['a'])
                        context['result'] = 'Квадратное уравнение имеет два действительных ' \
                                            'корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
                    elif discr == 0:
                        x = -context['b'] / (2 * context['a'])
                        context['result'] = 'Дискриминант равен нулю, квадратное уравнение имеет ' \
                                            'один действительный корень: x1 = x2 = %.1f' % x
                    else:
                        context['result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
                    context['discr'] = discr
            else:
                form = QuadraticForm()
                context['form'] = form
    return render(request, 'quadratic/results.html', context)
