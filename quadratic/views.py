# -*- coding:UTF-8 -*-
from django.shortcuts import render
import math


def quadratic_results(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    err_a, err_b, err_c = '', '', ''

    
    if a:
        if a.isdigit():
            if a == "0":
                err_a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            else:
                a = int(a)
        else:
            err_a = "коэффициент не целое число"
    else:
        err_a = "коэффициент не определен"
    
    if b:
        if b.isdigit():
            b = int(b)
        else:
            err_b = "коэффициент не целое число"
    else:
        err_b = "коэффициент не определен"
        
    if c:
        if c.isdigit():
            c = int(c)
        else:
            err_c = "коэффициент не целое число"
    else:
        err_c = "коэффициент не определен"

    discr_string = ''
    message = ''
    
    if not err_a and  not err_b and  not err_c:   
        discr = b**2 - 4 * a * c;
        discr_string = 'Дискриминант: % d' % discr
        if discr < 0:
            message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'
        elif discr == 0:
            x = -b/(2*a)
            message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
        else:
            x1 = (-b + discr**(1/2.0))/(2*a)
            x2 = (-b - discr**(1/2.0))/(2*a)
            message = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' %(x1, x2)
            
    return render(request,'quadratic/results.html',{'a': a,'err_a': err_a,\
                        'b': b,'err_b': err_b, 'c': c,'err_c': err_c,'d': discr_string,'msg':message })
