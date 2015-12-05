# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm


def quadratic_results(request):
    message = ''
    errors = {}
    x1 = x2 = descr = 0
    if not request.GET:
        form = QuadraticForm()
        return render(request, 'results.html', {'form': form})
    else:
        form = QuadraticForm(request.GET)
        a = request.GET.get('a')
        #if a==u'0':
            #errors['a'] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        if not form.errors:
            a = int(request.GET.get('a'))
            b = int(request.GET.get('b'))
            c = int(request.GET.get('c'))
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
            descr = "Дискриминант: " + str(descr)
            return render(request, 'results.html', {'message': message,'errors': errors, 
        'x1': x1, 'x2': x2, 'a': a, 'b': b, 'c': c, 'descr': descr, 'form': form})
        

        else:
            return render(request, 'results.html', {'form': form})
    
  