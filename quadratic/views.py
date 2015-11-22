 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
	err = False
	result = {}
	result['a'] = request.GET['a'] 
	result['b'] = request.GET['b']
	result['c'] = request.GET['c']
	result['diskr'] = ''
	result['a_att'] = ''
	result['b_att'] = ''
	result['c_att'] = ''
	result['diskr_att'] = ''
	for i in request.GET:
		att = i+'_att'
		if not request.GET[i].strip('-').isdigit() and request.GET[i] != "":
			result[att] = 'коэффициент не целое число'
			err = True
		elif len(request.GET[i]) == 0:
			result[att] = 'коэффициент не определен'
			err = True
	if request.GET['a'] == '0':
			result['a_att'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
			err = True
	if not err:
		a = int(result['a'])
		b = int(result['b'])
		c = int(result['c'])
		d = b**2 - 4*a*c
		result['diskr'] = "Дискриминант: " + str(d)
		
		if d<0:
			result['diskr_att'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		elif d == 0:
			x = -b/2*a
			result['diskr_att'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = " + str(round(x, 1))
		else:
			x1 = (-b + d**(1/2.0))/2*a
			x2 = (-b - d**(1/2.0))/2*a
			result['diskr_att'] = 'Квадратное уравнение имеет два действительных корня: x1 = '+str(x1)+", x2 = " +str(x2)
	return render(request, 'quadratic/results.html', result)
