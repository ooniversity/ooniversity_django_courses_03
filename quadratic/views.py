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
                err_a = "coefficient of a != 0"
            else:
                a = int(a)
        else:
            err_a = "coefficient is not int"
    else:
        err_a = "coefficient is not defined"
    
    if b:
        if b.isdigit():
            b = int(b)
        else:
            err_b = "coefficient is not int"
    else:
        err_b = "coefficient is not defined"
        
    if c:
        if c.isdigit():
            c = int(c)
        else:
            err_c = "coefficient is not int"
    else:
        err_c = "coefficient is not defined"

    discr_string = ''
    message = ''
    
    if not err_a and  not err_b and  not err_c:   
        discr = b**2 - 4 * a * c;
        discr_string = 'Discriminant: % d' % discr
        if discr < 0:
            message = 'Discriminant < 0. Quadratic equation has no solution'
        elif discr==0:
            x = -b/(2*a)
            message = 'Discriminant = 0. Quadratic equation has one real root: x1 = x2 = %.1f' % x
        else:
            x1 = (-b + discr**(1/2.0))/(2*a)
            x2 = (-b - discr**(1/2.0))/(2*a)
            message = 'Quadratic equation has two real roots: x1 = %.1f, x2 = %.1f' %(x1, x2)
            
    return render(request,'quadratic/results.html',{'a': a,'err_a': err_a,\
                        'b': b,'err_b': err_b, 'c': c,'err_c': err_c,'d': discr_string,'mes':message })
