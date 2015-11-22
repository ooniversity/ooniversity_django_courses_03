# -*- coding: utf-8 -*- 
from django.shortcuts import render


def quadratic_results(request):
	def get_discr(a, b, c):
		d = b**2 - 4*a*c
		return d
	
	get = request.GET
	
	my_dict = {'a': get['a'], 'b': get['b'], 'c': get['c']}

	error1 = "коэффициент не целое число"
	error2 = "коэффициент не определен"
	error3 = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
	
	try:
		a = int(my_dict['a'])
		b = int(my_dict['b'])
		c = int(my_dict['c'])
		d = get_discr(a, b, c)
		out = {'d': "Дискриминант: %s" %d}
		
		if a == 0:
			error3_a = {'error3_a': error3}
			my_dict.update(error3_a)
			return render(request, 'results.html', my_dict)

		if d < 0:
			my_dict['discr'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			my_dict.update(out)
			return render(request, 'results.html', my_dict)

		elif d == 0:
			x = -b / 2*a
			my_dict['discr'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % float(x)
			my_dict.update(out)
			return render(request, 'results.html', my_dict)

		else:
			x1 = (-b + d**(1/2.0)) / 2*a
			x2 = (-b - d**(1/2.0)) / 2*a
			my_dict['discr'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (float(x1), float(x2))
			my_dict.update(out)
			return render(request, 'results.html', my_dict)
		

	except ValueError:
		if my_dict['a'].isalpha():
			my_dict['error1_a'] = error1
        if my_dict['b'].isalpha():
            my_dict['error1_b'] = error1
        if my_dict['c'].isalpha():
            my_dict['error1_c'] = error1

        if my_dict['a']=='':
            my_dict['error2_a'] = error2
        if my_dict['b']=='':
            my_dict['error2_b'] = error2
        if my_dict['c']=='':
            my_dict['error2_c'] = error2

        return render(request, 'results.html', my_dict)
