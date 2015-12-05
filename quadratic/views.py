# -*- coding: utf-8 -*-
from django.shortcuts import render

from quadratic.forms import QuadraticForm

"""def quadratic_results(request):
	form = QuadraticForm()
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
		mes_a = u'коэффициент не определен'
		error = True
	else:
		if not a.isdigit() and '-' not in a:
			mes_a = u'коэффициент не целое число'
			error = True
		if int(a) == 0:
			mes_a = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
			error = True
			
	if not b:
		mes_b = u'коэффициент не определен'
		error = True
	elif not b.isdigit() and '-' not in b:
		mes_b = u'коэффициент не целое число'
		error = True
	if not c:
		mes_c = u'коэффициент не определен'
		error = True
	elif not c.isdigit() and '-' not in c:
		mes_c = u'коэффициент не целое число'
		error = True
	if not error:
		if '-' in a:
			a = -int(a[1:])
		else:
			a = int(a)
		if '-' in b:
			b = -int(b[1:])
		else:
			b = int(b)
		if '-' in c:
			c = -int(c[1:])
		else:
			c = int(c)
		discr = pow(b, 2.0) - 4 * a * c
		mes_discr = u'Дискриминант: %d' % discr
		if discr < 0:
			message = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			roots = ''
		elif discr == 0:
			x1 = x2 = round(float(-b / (2.0*a)),1)
			message = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
			roots = 'x1 = x2 = %s' % x1
		elif discr > 0:
			x1 = round(float((-b + (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			x2 = round(float((-b - (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			message = u'Квадратное уравнение имеет два действительных корня:'
			roots = 'x1 = %s, x2 = %s' % (x1, x2)
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'discriminant':mes_discr, 'message':message, 'roots':roots, 'mes_a':mes_a, 'mes_b':mes_b, 'mes_c':mes_c, 'form':form})
"""

def quadratic_results(request):
	result = {}
	message = None
	discr = None
	if request.GET:
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']

			discr = b * b - 4 * a * c
			if discr < 0:
				message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			elif discr == 0:
				x = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
				message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % x
			else:
				x1 = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
				x2 = round((-b - discr ** (1 / 2.0)) / 2 * a, 1)
				message = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (x1, x2)

			result['d'] = 'Дискриминант: %d' % discr
			result['message'] = message

	else:
		form = QuadraticForm()
	result['form'] = form
	return render(request, "quadratic/results.html", result)
