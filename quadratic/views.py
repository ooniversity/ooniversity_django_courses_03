 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm

def quadratic_results(request):
	result = {}
	msg = '' 
	if request.method == 'GET':
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			d = b**2 - 4*a*c
			if d < 0 :
				msg = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			elif d == 0:
				x =round(-b/2.0*a, 1)	
				msg = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % (x)
			else:
				x1 = (-b + d**(1/2.0) )/2*a
				x2 = (-b - d**(1/2.0) )/2*a
 				msg = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1,x2)
 			result['d'] = "Дискриминант: %s" %int(d)
 			result['msg'] = msg
 	else:
		form = QuadraticForm
	result['form'] = form
	return render(request, 'quadratic/results.html', result)