# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.defaulttags import register
from quadratic.forms import QuadraticForm

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key): 
        return dictionary.get(key)
    else:
        return ''

def quadratic_results(request):

    form = QuadraticForm()

    params = request.GET

    input_vars = ['a', 'b', 'c']
    vars_view = {}
    vars_msgs = {}
    vars_dict = {}
    discr = {}

    if request.method == 'GET':
        form = QuadraticForm(request.GET)

        for i in input_vars:
            vars_dict[i] = ''
            if i in params.keys():
                coef = params[i]
                vars_view[i] = coef

                try:
                    coef = int(coef)
                    vars_dict[i] = coef
                except ValueError:
                    vars_view[i] = coef
                    vars_dict[i] = ''
                    vars_msgs[i] = u'коэффициент не целое число'
                if coef == 0 and i == 'a':
                    vars_view[i] = 0
                    vars_dict[i] = ''
                    vars_msgs[i] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                if coef == '':
                    vars_view[i] = ''
                    vars_dict[i] = ''
                    vars_msgs[i] = u'коэффициент не определен'
            else:
                try:
                    a = params[i]
                except KeyError:
                    vars_view[i] = ''
                    vars_msgs[i] = u'коэффициент не определен'

        if vars_dict['a'] and vars_dict['b'] and vars_dict['c']:
            a = int(vars_dict['a'])
            b = int(vars_dict['b'])
            c = int(vars_dict['c'])

            D = b ** 2 - 4 * a * c

            if D < 0:    #a=1&b=12&c=38
                discr['D'] = u'Дискриминант: %d' % D
                discr['D_msg'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif D == 0: #a=1&b=6&c=9
                discr['D'] = u'Дискриминант: 0'
                x1 = x2 = -b / 2.0 * a
                discr['D_msg'] = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1
            else:        #a=-1&b=2&c=35
                discr['D'] = u'Дискриминант: %d' % D
                x1 = (-b + D ** (1/2.0)) / (2 * a)
                x2 = (-b - D ** (1/2.0)) / (2 * a)
                discr['D_msg'] = u'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
        else:
            pass

    return render(request, 'results.html',  {'values': sorted(vars_view.iteritems()), 'messages': vars_msgs, 'discr': discr, 'form': form})


