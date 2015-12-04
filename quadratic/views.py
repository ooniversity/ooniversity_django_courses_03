 # -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

# Create your views here.
def quadratic_results(request):
	dic = {}
	if request.method == "GET":
		form = QuadraticForm(request.GET or None)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			d = b**2 - 4*a*c
			if d > 0:
				x = (-b + d**(1/2.0))/(2*a)
				y = (-b - d**(1/2.0))/(2*a)
				dic['x'] = round(x, 1)
				dic['y'] = round(y, 1)
				dic['d'] = d
			elif d == 0:
				x = (-b + d**(1/2.0))/(2*a)
				dic['x'] = x
				dic['d'] = d
			else:
				dic['d'] = d
	else:
		form = QuadraticForm()
	return render(request, 'quadratic/results.html', {'form':form, 'dic':dic})