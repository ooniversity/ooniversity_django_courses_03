# -*- coding: utf-8 -*-
from django.shortcuts import render

def get_discriminant(request, a, b, c):
	res = pow(b, 2.0) - 4 * a * c
	return res

def quadratic_results(request):
	#s_new = s.split('&')
	a = request.GET.get('a')
	b = request.GET.get('b')
	c = request.GET.get('c').split('/')[0]
	mes_a = ''
	mes_b = ''
	mes_c = ''
	mes_discr = ''
	message = ''
	roots = ''
	error = False
	if not a:
		mes_a = u'коэффициент не определён'
		error = True
	else:
		if not a.isdigit() and '-' not in a:
			mes_a = u'коэффициент не целое число'
			error = True
		if int(a) == 0:
			mes_a = u'коэффициент при вервом слагаемом не может быть равным нулю'
			error = True
			
	if not b:
		mes_b = u'коэффициент не определён'
		error = True
	elif not b.isdigit() and '-' not in b:
		mes_b = u'коэффициент не целое число'
		error = True
	if not c:
		mes_c = u'коэффициент не определён'
		error = True
	elif not c.isdigit() and '-' not in c:
		mes_c = u'коэффициент не целое число'
		error = True
	if not error:
		if '-' in a:
			a = -int(a[1:])
		if '-' in b:
			a = -int(b[1:])
		if '-' in c:
			a = -int(c[1:])
		else:
			a = int(a)		
			b = int(b)
			c = int(c)
		discr = get_discriminant(request,a,b,c)
		mes_discr = u'Дискриминант: %d' % discr
		if discr < 0:
			message = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			roots = ''
		elif discr == 0:
			x1 = x2 = -b / (2*a)
			message = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
			roots = 'x1 = x2 = %d' % x1
		elif discr > 0:
			x1 = (-b + (b*b - 4*a*c)**(1/2.0)) / (2*a)
			x2 = (-b - (b*b - 4*a*c)**(1/2.0)) / (2*a)
			message = u'Квадратное уравнение имеет два действительных корня'
			roots = 'x1 = %d, x2 = %d' % (x1, x2)
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'discriminant':mes_discr, 'message':message, 'roots':roots, 'mes_a':mes_a, 'mes_b':mes_b, 'mes_c':mes_c})
	
