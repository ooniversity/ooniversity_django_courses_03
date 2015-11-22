# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
    errors = {}
    x1 = x2 = descr = 0
    message = ''
    request.GET
    a = request.GET.get('a')
    if a==u'0':
        errors['a'] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        #a = ''
    elif a and a[0] == '-' and a[1:].isdigit():
        a = int(request.GET.get('a'))
    elif a.isdigit():
        a = int(request.GET.get('a'))
    else:
        if a =='':
            errors['a'] = "коэффициент не определен"
        else:
            errors['a'] = "коэффициент не целое число"
            #a = ''

    b = request.GET.get('b')
    if b and b[0] == '-' and b[1:].isdigit():
        b = int(request.GET.get('b'))
    elif b.isdigit():
        b = int(request.GET.get('b'))
    else:
        if b == '':
            errors['b'] = "коэффициент не определен"
        else:
            errors['b'] = "коэффициент не целое число"
            #b = ''

    c = request.GET.get('c')
    if c and c[0] == '-' and c[1:].isdigit():
        c = int(request.GET.get('c'))
    elif c.isdigit():
        c = int(request.GET.get('c'))
    else:
        if c == '':
            errors['c'] = "коэффициент не определен"
        else:
            errors['c'] = "коэффициент не целое число"
            #c = ''
    
    if not errors:
        descr = (b**2 - 4*a*c)
        if descr >= 0:
            x1 = (-b + descr**0.5)/ 2*a
            x2 = (-b - descr**0.5) / 2*a
    if descr<0: 
        message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif descr==0:
        message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1
    else:
        message = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
    return render(request, 'results.html', {'message': message,'errors': errors, 
        'x1': x1, 'x2': x2, 'a': a, 'b': b, 'c': c, 'descr': int(descr)})


