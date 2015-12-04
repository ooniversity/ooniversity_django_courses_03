# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm

def get_discr (a,b,c):
    d=b**2-4*a*c
    return d
	
def quadratic_results(request):
	dic = {}
	print 'hara'
	if request.method == "GET":
		form = QuadraticForm(request.GET)	
		if form.is_valid():
			print 'vali	d'
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			x1 = 0
			x2 = 0
			discr = get_discr(a,b,c)
			if discr==0:
				x1 = x2 = (-1)*b/2*a
				dic['x1'] = x1
				dic['x2'] = x2
				dic['discr'] = discr
			else: 
				x1=((-1)*b+discr**(1/2))/(2*a)
				x2=((-1)*b-discr**(1/2))/(2*a)
				dic['x1'] = x1
				dic['x2'] = x2
				dic['discr'] = discr
			print discr
		else:
			print 'not valid'
			form = QuadraticForm(request.GET)
	else:
		print 'not get'
		form = QuadraticForm(request.GET)
	
	return render(request,'quadratic/results.html', {'dic':dic, 'form':form})
