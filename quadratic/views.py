# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from forms import QuadraticForm

def discr(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  d=(b*b)-(4*a*c)
  return d

def tworoots(request, a, b, c):
  a = float(a)
  b = float(b)
  c = float(c)
  x1=(-b+((b*b-4*a*c)**(1/2.0)))/2*a
  x2=(-b-((b*b-4*a*c)**(1/2.0)))/2*a
  x1=round(x1,2)
  x2=round(x2,2)
  t=u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s ' % (x1,x2)
  return t

def oneroot(request, a, b, c):
  x=-float(b)/(2*float(a))
  t=u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
  return t

def quadratic_results(request):
  form = QuadraticForm()
  a = request.GET['a']
  b = request.GET['b']
  c = request.GET['c']
  koef = {'a': a, 'b': b, 'c': c}
  answer = {}
  for i in koef.keys():
    if not koef[i]:
      k = 'answer_' + i
      answer[k] = u'коэффициент не определен'
    else:
      try:
        koef[i] = int(koef[i])
      except Exception:
        k = 'answer_' + i
        answer[k] = u'коэффициент не целое число'
  if koef['a'] == 0:
    answer['answer_a'] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
  if len(answer) == 0:
    d = answer['answer_d']=discr(request,a,b,c)
    if d == 0:
      answer['xx'] = oneroot(request, a, b, c)
    elif d < 0:
      answer['error_d'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
      answer['xx'] = tworoots(request, a, b, c)
  answer.update(koef)
  answer['form'] = form
  return render(request,'results.html', answer)

