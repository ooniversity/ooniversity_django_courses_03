# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm

def quadratic_results(request):     
    form = QuadraticForm()
    d = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            discriminant = count_discriminant(**data)
            if discriminant < 0:
                result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif discriminant == 0:
                x = (- data['b']) / (2.0 * data['a'])
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % str(x)
            else:
                x1 = (- data['b'] + discriminant**0.5) / (2.0 * data['a'])
                x2 = (- data['b'] - discriminant**0.5) / (2.0 * data['a'])
                result_message = "Квадратное уравнение имеет два действительных корня: x1 = " + str(x1) + ", x2 = " + str(x2)
            d.update({'discriminant': discriminant, 'message': result_message})
    else:
        form = QuadraticForm()
    d.update({'form':form}) 
    return render(request, 'quadratic/results.html', d)


def count_discriminant(**kwargs):
    a, b, c = float(kwargs['a']), float(kwargs['b']), float(kwargs['c'])
    d = b**2.0 - 4.0 * a * c
    return int(d)