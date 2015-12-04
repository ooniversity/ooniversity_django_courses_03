# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def discr(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  d=(b*b)-(4*a*c)
  return d

def quadratic_results(request):
    answer = {}
    massage = None
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
          a = form.cleaned_data['a']
          b = form.cleaned_data['b']
          c = form.cleaned_data['c']
          d= discr(request, a, b, c)
          if d < 0:
            message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
          elif d == 0:
            x = round((-b + d**(1/2.0)) / 2*a, 1)
            message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x
          else:
            x1 = round((-b + d**(1/2.0)) / 2*a, 1)
            x2 = round((-b - d**(1/2.0)) / 2*a, 1)
            message = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1,x2)
          
          answer['d'] = 'Дискриминант: %d'  %d
          answer['message'] = message
        else:
            answer['message'] = u'коэффициент не целое число'
    else:
        form = QuadraticForm()
    answer['form'] = form
    return render(request,'quadratic/results.html', answer)