
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from quadratic.forms import QuadraticForm



def quadratic_results(request):
	strdiscr=''
	message=''
	if request.method == 'GET':
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
			discr = b**2-4*a*c
			strdiscr = 'Дискриминант: % d' % discr
			if discr < 0:
				message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'
			elif discr==0:
				x =  -b/2*a
				message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
			else:
				x1=(-b+ discr**(1/2.0))/(2*a)
				x2=(-b- discr**(1/2.0))/(2*a)
				message = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' %(x1,x2)
	else:
		form = QuadraticForm()
		
			
	return render(request,'quadratic/results.html',{'d': strdiscr,'mes':message, 'form':form })
	
