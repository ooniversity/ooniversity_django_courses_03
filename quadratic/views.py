# -*- coding: utf-8 -*-
from django.shortcuts import render

def self_check(x):
    y = ''
    if x.replace('-', '').isdigit()==False:
        if x=='':
            y = "коэффициент не определен"
        else:
            y  = "коэффициент не целое число"
    return y

def quadratic_results(request):
    var_a=request.GET['a']
    var_b=request.GET['b']
    var_c=request.GET['c']
    a_error = ''
    b_error = ''
    c_error = ''
    d_text = ''
    if self_check(var_a):
        a_error = self_check(var_a)
    elif int(var_a)==0:
        a_error = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
    if self_check(var_b):
        b_error = self_check(var_b)
    if self_check(var_c):
        c_error = self_check(var_c)
    if a_error or b_error or c_error:
        d = ''
        x1 = x2 = ''
    else:
        d = int(var_b)**2 - 4*int(var_a)*int(var_c)
        if d < 0:
            d_text = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            x1 = x2 = ''
        elif d == 0:
            x1 = x2 = (-float(var_b) + d ** (1/2.0))/ 2.0*float(var_a)
            d_text = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %r" %x1
        else:
            x1 = (-float(var_b) + d ** (1/2.0))/ 2.0*float(var_a)
            x2 = (-float(var_b) - d ** (1/2.0))/ 2.0*float(var_a)
            d_text = "Квадратное уравнение имеет два действительных корня: x1 = %r, x2 = %r" % (x1, x2)

            
    return render(request, "results.html", {'a': var_a, 'b': var_b, 'c':var_c, 'a_bad': a_error, 'b_bad': b_error, 'c_bad': c_error, 'd': d, 
'd_bad': d_text, 'x1':x1, 'x2':x2})
