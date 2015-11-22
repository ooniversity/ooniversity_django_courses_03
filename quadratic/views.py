# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse



def quadratic_results(request):
    
    a = request.GET['a']
    a_error = ''

    if a:
        if a.replace("-", "").isdigit():
            if a == "0":
                a_error = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            else:
                a = int(a)
        else:
            a_error = "коэффициент не целое число"
    else:
        a_error="коэффициент не определен"
    
    b = request.GET['b']
    b_error = ""

    if b:
        if b.replace("-", "").isdigit():
            b = int(b)
        else:
            b_error = "коэффициент не целое число"
    else:
        b_error="коэффициент не определен"
        
    c = request.GET['c']
    c_error = ""

    if c:
        if c.replace("-", "").isdigit():
            c = int(c)
        else:
            c_error = "коэффициент не целое число"
    else:
        c_error="коэффициент не определен"
    strdiscr=''
    message=''
        
    
    if not a_error and  not b_error and  not c_error:   
        discr = b**2-4*a*c
        strdiscr = 'Дискриминант: % d' % discr
        if discr < 0:
            message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'
        elif discr==0:
            x =  -b/2*a
            message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
        else:
            x1=(-b+ discr**(1/2.0))/(2*a)
            x2=(-b- discr**(1/2.0))/(2*a)
            message = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' %(x1,x2)
            
    return render(request,'quadratic/results.html',{'a': a,'a_error': a_error,'b': b,'b_error': b_error, 'c': c,'c_error': c_error,'d': strdiscr,'mes':message })
    