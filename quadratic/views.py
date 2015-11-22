 # -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def quadratic_results(request):
	a = request.GET.get('a', '')
	b = request.GET.get('b', '')
	c = request.GET.get('c', '')
	error = ''
	result = ''
	int_error = ''
	d=''
	x = ''
	y = ''
	dic = {a:"", b:"", c:""}
	if (a.isdigit() and b.isdigit() and c.isdigit() and (int(a) != 0)) == True:
		a = int(a)
		b = int(b)
		c = int(c)
		d = b**2 - 4*a*c
		if d > 0:
			x = (-b + d**(1/2))/(2*a)
			y = (-b - d**(1/2))/(2*a)
			x=round(x, 1)
			y=round(y, 1)
			result = 'Квадратное уравнение имеет два действительных корня:'
		elif d == 0:
			x = (-b + d**(1/2))/(2*a)
			x=round(x, 1)
			y = ''
			result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень x1=x2:'
		elif d < 0:
			result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			x = ''
			y = ''
	else:
		list_int = [a, b, c]
		for l in list_int:
			if l == "":
				dic[l] = "коэффициент не определен"
			elif l.isdigit() == False:
				dic[l] = "коэффициент не целое число"
			else:
				dic[l] = ""
		if list_int[0].isdigit() and list_int[0] == 0:
				dic['a'] = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"
		else:
			pass
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'd':d, 'result':result, 'dic':dic, 'x':x, 'y':y})