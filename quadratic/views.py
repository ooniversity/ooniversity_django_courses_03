# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
	return render(request, 'results.html')

def quadratic_results(request):
	yravnenie = "Квадратное уравнение a*x*x + b*x + c = 0"
	def get_discr(a, b, c):
		d = b**2 - 4*a*c
		return d
	
	r = request.GET
	
	dictionary = {'a': str(r['a']), 'b': str(r['b']), 'c': str(r['c'])}

	error_mess1 = "коэффициент не целое число"
	error_mess2 = "коэффициент не определен"
	error_mess3 = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
	
	try:
		a = int(dictionary['a'])
		b = int(dictionary['b'])
		c = int(dictionary['c'])
		d = get_discr(a, b, c)
		outp_d = {'d': "Дискриминант: %s" %d}
		
		if a == 0:
			error_mess3_a = {'error_mess3_a': error_mess3}
			dictionary.update(error_mess3_a)
			return render(request, 'results.html', dictionary)

		if d < 0:
			dictionary['discr'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			dictionary.update(outp_d)
			return render(request, 'results.html', dictionary)

		elif d == 0:
			x = -b / 2*a
			dictionary['discr'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % float(x)
			dictionary.update(outp_d)
			return render(request, 'results.html', dictionary)

		else:
			x1 = (-b + d**(1/2.0)) / 2*a
			x2 = (-b - d**(1/2.0)) / 2*a
			dictionary['discr'] = "Квадратное уравнение имеет два действительных корня: x1 = %s x2 = %s" % (float(x1), float(x2))
			dictionary.update(outp_d)
			return render(request, 'results.html', dictionary)
		

	except ValueError:
		if dictionary['a'].isalpha():
			dictionary['error_mess1_a'] = error_mess1
        if dictionary['b'].isalpha():
            dictionary['error_mess1_b'] = error_mess1
        if dictionary['c'].isalpha():
            dictionary['error_mess1_c'] = error_mess1

        if dictionary['a']=='':
            dictionary['error_mess2_a'] = error_mess2
        if dictionary['b']=='':
            dictionary['error_mess2_b'] = error_mess2
        if dictionary['c']=='':
            dictionary['error_mess2_c'] = error_mess2

        return render(request, 'results.html', dictionary)

