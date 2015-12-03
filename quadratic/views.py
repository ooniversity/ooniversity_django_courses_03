# -*- coding: utf-8 -*- 
from django.shortcuts import render
from forms import QuadraticForm

	
def quadratic_results(request):
	print request.GET, request.method
	if request.method == 'GET':
		form = QuadraticForm(request.GET)
		if form.is_valid():
			def get_discr(a, b, c):
				d = b**2 - 4*a*c
				return d
	
			get = request.GET
	
			my_dict = {'a': get['a'], 'b': get['b'], 'c': get['c']}

			a = int(my_dict['a'])
			b = int(my_dict['b'])
			c = int(my_dict['c'])
			d = get_discr(a, b, c)
			out = {'d': "Дискриминант: %s" %d}
		
			#if a == 0:
				#b = clean_a(0)
				#return b
				#my_dict['form'] = form
				#my_dict['error_2'] = get['a']
		
			if d < 0: 
				my_dict['d'] = d
				my_dict['form'] = form
				my_dict.update(out)

			elif d == 0:
				x = -b / 2*a
				my_dict['x1'] = round(x, 1)
				my_dict['d'] = d
				my_dict['form'] = form
				my_dict.update(out)

			else:
				x1 = (-b + d**(1/2.0)) / 2*a
				x2 = (-b - d**(1/2.0)) / 2*a
				my_dict['x1'] = round(x1, 1)
				my_dict['x2'] = round(x2, 1)
				my_dict['d'] = d
				my_dict['form'] = form	
				my_dict.update(out)
			return render(request, 'quadratic/results.html', my_dict)
		else:
			#form = QuadraticForm(request.GET)
			return render(request, 'quadratic/results.html', {'form': form})
	else:
		form = QuadraticForm()
	return render(request, 'quadratic/results.html', {'form': form})
