 #-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
def quadratic_results(request): 
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    res={'a': a,'b': b, 'c': c}   
    
    if res['a'] == '':            
        res['erra'] = str('коэффициент не определен')
    elif int(a) == 0:
            
        res['erra'] = str('коэффициент при первом слагаемом уравнения не может быть равным нулю')
    
    if res['b'] == '':            
        res['errb'] = str('коэффициент не определен')
    elif b.replace('.', '').replace('-', '').isdigit() != True:
        res['errb'] = str('коэффициент не целое число')
    if res['c'] == '':            
        res['errc'] = str('коэффициент не определен')
    elif c.replace('.', '').replace('-', '').isdigit() != True:
        res['errc'] = str('коэффициент не целое число')
    
                    
    if a.replace('.', '').replace('-', '').isdigit() and float(a) != 0:
        if b.replace('.', '').replace('-', '').isdigit() and float(b) != 0:
            if c.replace('.', '').replace('-', '').isdigit() and float(c) != 0:
                a = int(a)
                b = int(b)
                c = int(c)
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
        
            

                    
    
   
        
           
            
       
      
    return render(request,'results.html',res)

   
