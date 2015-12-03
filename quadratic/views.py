 #-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm
def quadratic_results(request): 
    form = QuadraticForm()
    res={}   
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            discr = b**2 - 4*a*c
            if discr == 0:
                res['d'] = str('Дискриминант: %d' % discr)
                x = -b/ 2.0*a
                res['x'] = str('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x)
            if discr < 0:
                res['d'] = str('Дискриминант: %d' % discr)
                res['x'] = str('Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
            if discr > 0:
                res['d'] = str('Дискриминант: %d' % discr)
                x1 = str((-b + discr ** (1/2.0)) / 2*a)
                x2 = str((-b - discr ** (1/2.0)) / 2*a)
                res['x'] = str('Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2))
   
       
    res['form'] = form
    return render(request,'results.html',res)

   
