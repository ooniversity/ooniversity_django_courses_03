# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import math


def quadratic_results(request):
	income_values = {"a" : [request.GET["a"], ""], "b" : [request.GET["b"], ""], "c" : [request.GET["c"], ""]}

    for item in income_values:
        if income_values[item][0] == "":
        	error_one = "коэффициент не определен"
        elif int(a) == 0:
        	error_one = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

        if income_values[item][1] = "":
        	error_two = "коэффициент не определен"
        elif b.replace('.', '').replace('-', '').isdigit() != True:
        	error_two = "коэффициент не целое число"
        if income_values[item][2] = "":
        	error_three = "коэффициент не целое число"
        elif b.replace('.', '').replace('-', '').isdigit() != True:
        	error_three = "коэффициент не целое число"

	
    if a.replace('.', '').replace('-', '').isdigit() and float(a) != 0:
    	if b.replace('.', '').replace('-', '').isdigit() and float(b) != 0:
    		if c.replace('.', '').replace('-', '').isdigit() and float(c) != 0:
				a = float(a)
				b = float(b)
				c = float(c)
				discriminant = b**2 - 4*a*c
				printed_message = ""

				if d < 0:
					printed_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
				elif d == 0:
					x = -b / (2 * a)
					printed_message "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % x
				elif d > 0:
					x1 = (-b + math.sqrt(d)/(2*a))
				    x2 = (-b - math.sqrt(d)/(2*a))
				    printed_message "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (x1, x2)