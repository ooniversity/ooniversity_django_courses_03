 #-*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request): 
    form = QuadraticForm()
    context={}   
    if request.method == 'GET':
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            discr = b**2 - 4*a*c
            
            if discr == 0:
                context['d'] = discr
                x = -b/ 2.0*a
                context['message'] = str('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x)
            if discr < 0:
                context['d'] = discr
                context['message'] = str('Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
            if discr > 0:
                context['d'] = discr
                x1 = str((-b + discr ** (1/2.0)) / 2*a)
                x2 = str((-b - discr ** (1/2.0)) / 2*a)
                context['message'] = str('Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2))
   
    else:
        form = QuadraticForm()       
    context['form'] = form
    return render(request,'quadratic/results.html', context)

   
