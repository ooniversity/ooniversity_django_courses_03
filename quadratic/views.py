 #-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import math


def quadratic_results(request): 
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    income_values={'a': a,'b': b, 'c': c}

    if income_values['a'] == '':            
        income_values['err1'] = 'коэффициент не определен'
    elif int(a) == 0:            
        income_values['err1'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'    
    if income_values['b'] == '':            
        income_values['err2'] = 'коэффициент не определен'
    elif b.replace('.', '').replace('-', '').isdigit() != True:
        income_values['err2'] = 'коэффициент не целое число'
    if income_values['c'] == '':            
        income_values['err3'] = 'коэффициент не определен'
    elif c.replace('.', '').replace('-', '').isdigit() != True:
        income_values['err3'] = 'коэффициент не целое число'

                    
    if a.replace('.', '').replace('-', '').isdigit() and float(a) != 0:
        if b.replace('.', '').replace('-', '').isdigit() and float(b) != 0:
            if c.replace('.', '').replace('-', '').isdigit() and float(c) != 0:
                a = float(a)
                b = float(b)
                c = float(c)
                discr = b**2 - 4*a*c
                if discr == 0:
                    income_values['d'] = str('Дискриминант: %d' % discr)
                    x = -b / (2 * a)
                    income_values['x'] = str('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x)
                if discr < 0:
                    income_values['d'] = str('Дискриминант: %d' % discr)
                    income_values['x'] = str('Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
                if discr > 0:
                    income_values['d'] = str('Дискриминант: %d' % discr)
                    x1 = (-b + math.sqrt(discr)) / (2 * a)
                    x2 = (-b - math.sqrt(discr)) / (2 * a)
                    income_values['x'] = str('Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2))     
    return render(request,'results.html', income_values)