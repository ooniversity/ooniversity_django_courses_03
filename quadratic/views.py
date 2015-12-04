# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm

def get_discr (a,b,c):
    d=b**2-4*a*c
    return d
	
def quadratic_results(request):
	dic = {}
	if request.method == "GET":
		form = QuadraticForm(request.GET)	
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			x1 = 0
			x2 = 0
			d = get_discr(a,b,c)
			if d==0:
				x1 = x2 = (-1)*b/2*a
				dic['x1'] = round(x1, 1)
				dic['x2'] = round(x1, 1)
				dic['d'] = d
			elif d>0: 
				x1=(-b + d**(1/2.0))/(2.0*a)
				x2=(-b - d**(1/2.0))/(2.0*a)
				dic['x1'] = x1
				dic['x2'] = x2
				dic['d'] = d
			else:
				dic['d'] = d
	else:
		form = QuadraticForm()
	
	return render(request,'quadratic/results.html', {'dic':dic, 'form':form})
