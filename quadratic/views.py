# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.defaulttags import register
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    quad_form = QuadraticForm(request.GET)
    context = {}
    #  and any(coef != '' for coef in form)
    if quad_form.is_valid():
        a = quad_form.cleaned_data['a']
        b = quad_form.cleaned_data['b']
        c = quad_form.cleaned_data['c']

        # calculate Discriminant

        discr = b ** 2.0 - 4.0 * a * c

        d_msg = u'Дискриминант: %d' % discr

        context = {'discr': d_msg}

        # calculate Roots

        if discr < 0:  # a=1&b=12&c=38
            context['res'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif discr == 0:  # a=1&b=6&c=9
            x1 = -b / 2.0 * a
            context['res'] = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1
        else:  # a=-1&b=2&c=35
            x1 = (-b + discr ** (1 / 2.0)) / (2 * a)
            x2 = (-b - discr ** (1 / 2.0)) / (2 * a)
            context['res'] = u'Квадратное уравнение имеет два действительных корня: x1 = %.2f, x2 = %.2f' % (x1, x2)

    elif any(coef == '' for coef in quad_form):  # if missing coef found call form
        quad_form = QuadraticForm()

    context['form'] = quad_form
    return render(request, 'quadratic/results.html', context)
