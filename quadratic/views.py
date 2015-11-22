 # -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def quadratic_results(request):
	a = request.GET.get('a', '')
	b = request.GET.get('b', '')
	c = request.GET.get('c', '')
	error_a = ""
	error_b = ""
	error_c = ""
	result = ''
	d=''
	x = ''
	y = ''
	dic = {a:"", b:"", c:""}
	if (a.lstrip('-').isdigit() and b.replace('-', '').isdigit() and c.replace('-', '').isdigit() and (a != '0')) == True:
		a = int(a)
		b = int(b)
		c = int(c)
		d = b**2 - 4*a*c
		if d > 0:
			x = (-b + d**(1/2.0))/(2*a)
			y = (-b - d**(1/2.0))/(2*a)
			#x=round(x, 1)
			#y=round(y, 1)
			result = 'Квадратное уравнение имеет два действительных корня: %d, %d' %(x, y)
		elif d == 0:
			x = (-b + d**(1/2))/(2*a)
			#x=round(x, 1)
			#y = ''
			result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень x1=x2: %d' %(x)
		elif d < 0:
			result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
	else:
		list_int = [a, b, c]
		if list_int[0] == '0':
				dic[a] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
				for l in list_int[1:]:
					if l == "":
						dic[l] = "коэффициент не определен"
					elif l.replace('-', '').isdigit() == False:
						dic[l] = "коэффициент не целое число"
					else:
						dic[l] = ""
		else:
			for l in list_int:
				if l == "":
					dic[l] = "коэффициент не определен"
				elif l.replace('-', '').isdigit() == False:
					dic[l] = "коэффициент не целое число"
				else:
					dic[l] = ""
			else:
				pass
		error_a = dic[a]
		error_b = dic[b]
		error_c = dic[c]
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'd':d, 'result':result, 'error_a':error_a, 'error_b':error_b, 'error_c':error_c})