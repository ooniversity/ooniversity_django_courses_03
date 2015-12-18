# -*- coding: utf-8 -*- 
from django.shortcuts import render
from quadratic.forms import QuadraticForm

	
def quadratic_results(request):
	context = {}
	if request.GET:
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']	
			D = b * b - 4 * a * c
			if D < 0:
				context['D'] = D
			elif D == 0:
				x = (-b + D**(1/2.0)) / 2*a
				context['x1'] = round(x, 1)
				context['D'] = D
			else:
				x1 = (-b + D**(1/2.0)) / 2*a
				x2 = (-b - D**(1/2.0)) / 2*a
				context['x1'] = round(x1, 1)
				context['x2'] = round(x2, 1)
				context['D'] = D			
	else:
		form = QuadraticForm()
	return render(request, 'quadratic/results.html', {'form': form, 'context': context})


