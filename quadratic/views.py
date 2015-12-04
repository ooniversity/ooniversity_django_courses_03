 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm

def quadratic_results(request):
	result = {}
	if request.method == 'GET':
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			d = b**2 - 4*a*c
			if d >=0 :
				x0 = round(-b/2.0*a, 1)	
				x1 = (-b + d**(1/2.0))/2*a
				x2 = (-b - d**(1/2.0))/2*a
				result = {'d': d, 'a': a, 'x0': x0, 'x1': x1, 'x2': x2}
			else:
				result = {'d':d , 'a': a}
	else:
		form = QuadraticForm
	result['form'] = form
	return render(request, 'quadratic/results.html', result)