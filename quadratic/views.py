# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()

def quadratic_results(request):
    form = QuadraticForm()
    #a = int(request.GET['a'])
    #b = int(request.GET['b'])
    #c = int(request.GET['c'])
    #print a, b, c
    x = x1 = x2 = None
    d = b ** 2 - 4 * a * c 
    if d < 0:
        pass #result = 'Дискриминант: %d Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.' % d
    elif d == 0:
        x = -b / 2*a
        #result = 'Дискриминант: 0 Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %d' % x
    else:
        x1 = (-b + d ** (1/2.0)) / (2*a)
        x2 = (-b - d ** (1/2.0)) / (2*a)
        #result = "Дискриминант: %d Уравнение имеет два действительных корня: x1 = %d, x2 = %d" % (d, x1, x2)
    return render(request, 'results.html', {"a": a, "b": b, "c": c, "d": d, 'x': x, "x1": x1, "x2": x2, "form": form})
