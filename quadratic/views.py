 # -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

# Create your views here.
def quadratic_results(request):
	a = ''
	b = ''
	c = ''
	error_a = ""
	error_o = ""
	error_b = ""
	error_c = ""
	result = ''
	result_d = ''
	d=''
	x = ''
	y = ''
	#form = QuadraticForm()
	if request.method == "GET":
		form = QuadraticForm(request.GET or None)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			d = b**2 - 4*a*c
			#d=round(d, 1)
			result_d = 'Дискриминант: %s' %(d)
			if d > 0:
				x = (-b + d**(1/2.0))/(2*a)
				y = (-b - d**(1/2.0))/(2*a)
				result = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' %(x, y)
			elif d == 0:
				x = (-b + d**(1/2.0))/(2*a)
				result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' %(x)
			elif d < 0:
				result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
	else:
		form = QuadraticForm()
	return render(request, 'quadratic/results.html', {'form':form, 'result_d':result_d, 'result':result, 'error_o':error_o, 'error_a':error_a, 'error_b':error_b, 'error_c':error_c})