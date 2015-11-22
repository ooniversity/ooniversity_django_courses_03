# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	error_1 = "коэффициент не определен"
	error_2 = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
	error_3 = "коэффициент не целое число"
	data = {'a' : a, 'b' : b, 'c' : c}

	def error_check(arg):
		out =None
		if arg == '':
			out = error_1
		elif arg.replace('.', '').replace('-', '').isdigit() == False:
			out = error_3
		elif arg[0] != '-' and not arg.isdigit():
			out = error_3	
		return out
		
	def discr(a, b, c):
		d = pow(b, 2) - 4*a*c
		return d

	if error_check(a) is not None:
		data['error_a'] = error_check(a)
	elif int(a) == 0:
		data['error_a'] = error_2
	if error_check(b) is not None:
		data['error_b'] = error_check(b)
	if error_check(c) is not None:
		data['error_c'] = error_check(c)
	if not (data.get('error_a') or data.get('error_b') or data.get('error_c')):
		d = discr(int(a), int(b), int(c))
		data['print_d'] = "Дискриминант: %(d)d" % { 'd':d }
		if d < 0:
			data['d_out'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		if d == 0:
			x = -int(b) / 2*int(a)
			data['d_out'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % float(x)
		if d > 0:
			x1 = (-int(b) + d ** (1/2.0)) / 2*int(a)
			x2 = (-int(b) - d ** (1/2.0)) / 2*int(a)
			data['d_out'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (float(x1), float(x2))
	return render(request, 'results.html', data)
	