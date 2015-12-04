# -*- coding: utf-8 -*-
import math
from django.shortcuts import render
from quadratic.forms import QuadraticForm



def quadratic_results(request):
    context = {}

    if request.GET.get('a') is None and request.GET.get('b') is None and request.GET.get('c') is None:
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.GET)

    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']

        d = round((math.pow(b, 2) - 4 * a * c), 2)

        if d > 0:
            x1 = round(((-b + math.sqrt(d)) / (2.0 * a)), 2)
            x2 = round(((-b - math.sqrt(d)) / (2.0 * a)), 2)
            context['result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}'.format(x1, x2)
        elif d == 0:
            x1 = round((-b / (2.0 * a)), 2)
            context['result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}'.format(x1)
        elif d < 0:
            context['result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

        context['D'] = 'Дискриминант: {0}'.format(d)

    context['form'] = form
    return render(request, 'results.html', context)