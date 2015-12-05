# -*- coding: utf-8 -*-
from django.shortcuts import render
from form import QuadraticForm

def quadratic_results(request):
    main_result = {}
    form = QuadraticForm()
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            d = b**2-4*a*c
            main_result['d'] = int(d)
            if d < 0:
                main_result['mistake_d'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif not d:
                result = -b/2*a
                main_result['result'] = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % result
            else:
                x1 = (- b + d ** (1 / 2.0)) / 2 * a
                x2 = (- b - d ** (1 / 2.0)) / 2 * a
                result = u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (round(x1, 2), round(x2, 2))
                main_result['result'] = result
    main_result['form'] = form
    return render(request,'results.html', main_result)

