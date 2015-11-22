# -*- coding: utf-8 -*-
from django.shortcuts import render

def get_discr (a,b,c):
    d=b**2-4*a*c
    return d
	
def quadratic_results(request):
	a = request.GET['a']  
	b = request.GET['b']  
	c = request.GET['c']    
	a_error = ''
	b_error = ''
	c_error = ''
	strdiscr = ''
	mes = ''
	x1 = 0
	x2 = 0
	if a=='':
		a_error = 'коэффициент не определен'
	if b=='':
		b_error = 'коэффициент не определен'
	if c=='':
		c_error = 'коэффициент не определен'
	if a=='0':
		a_error = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
	if not a.replace('.', '').isdigit() and len(a)<>0 and a_error =='' and a[0]<>'-':
		a_error = 'коэффициент не целое число'
	if not b.replace('.', '').isdigit() and len(b)<>0 and b_error ==''and b[0]<>'-':
		b_error = 'коэффициент не целое число'
	if not c.replace('.', '').isdigit() and len(c)<>0 and c_error ==''and c[0]<>'-':
		c_error = 'коэффициент не целое число'

	if a_error =='' and b_error =='' and c_error =='':
		discr = get_discr(float(a),float(b),float(c))
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
	return render(request,'quadratic/results.html', {'a':a, 'a_error':a_error,'b':b, 'b_error':b_error,'c':c, 'c_error':c_error, 'd':strdiscr, 'mes':mes})
