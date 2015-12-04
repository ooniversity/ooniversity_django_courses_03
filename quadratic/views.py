# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm

def get_discr (a,b,c):
    d=b**2-4*a*c
    return d
	
def quadratic_results(request):
	strdiscr = ''
	mes = ''
	if request.method == "GET":
		form = QuadraticForm(request.GET)	
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			discr = get_discr(a,b,c)
			if discr==0:
				strdiscr = 'Дискриминант: 0' 
				x1 = (-1.0)*float(b)/2*float(a)
				mes = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1
			elif discr<0:
				strdiscr = 'Дискриминант: %d'%discr 
				mes = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			else: 
				x1=((-1)*float(b)+discr**(1/2.0))/(2*float(a))
				x2=((-1)*float(b)-discr**(1/2.0))/(2*float(a))
				mes = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' %(x1,x2)
				strdiscr = 'Дискриминант: %d'%discr
	else:
		form = QuadraticForm()
	return render(request,'quadratic/results.html', {'d':strdiscr, 'mes':mes, 'form':form})
