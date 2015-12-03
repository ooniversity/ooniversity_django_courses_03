
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from quadratic.forms import QuadraticForm



def quadratic_results(request):
	form = QuadraticForm()
	strdiscr=''
	
	
	message=''
	if form.is_valid():
		data=form.cleaned_data

		a = request.GET['a']
	#a_error = ''

	#if a:
		#p = a.replace("-", "")
		#if p.isdigit():
			#if a == "0":
				#a_error = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
			#else:
				#a = int(a)
		#else:
			#a_error = "коэффициент не целое число"
	#else:
		#a_error="коэффициент не определен"
	
		b = request.GET['b']
	#b_error = ""

	#if b:
		#p = b.replace("-", "")
		#if p.isdigit():
			#b = int(b)
		#else:
			#b_error = "коэффициент не целое число"
	#else:
		#b_error="коэффициент не определен"
        
		c = request.GET['c']
	#c_error = ""

	#if c:
		#p = c.replace("-", "")
		#if p.isdigit():
			#c = int(c)
		#else:
			#c_error = "коэффициент не целое число"
	#else:
		#c_error="коэффициент не определен"

	   	
	
 	#if not a_error and  not b_error and  not c_error:	
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
			
	return render(request,'quadratic/results.html',{'d': strdiscr,'mes':message, 'form':form })
	
