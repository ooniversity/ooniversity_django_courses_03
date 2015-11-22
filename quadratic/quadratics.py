# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math



def quadratic(parametr_list):
    flag = True
    new_list = {}
    new_list['a'] = parametr_list["a"]
    new_list['b'] = parametr_list["b"]
    new_list['c'] = parametr_list['c']
    new_list['a_error'] = ""
    new_list['b_error'] = ""
    new_list['c_error'] = ""
    new_list['d'] = ""
    new_list['d_error'] = ""
    for key in parametr_list:
        digit_coeff = str(parametr_list[key]).strip("-").isdigit()
        str_coeff = not str(parametr_list[key]).strip("-").isdigit()
        error = key+'_error'
        if str_coeff and (not parametr_list[key] == ""):
            flag = False
            new_list[error] = 'коэффициент не целое число'
        elif parametr_list[key] == "":
            flag = False
            new_list[error] ='коэффициент не определен'
        elif digit_coeff and key == "a" and int(parametr_list[key]) == 0:
            flag = False
            new_list[error] ='коэффициент при первом слагаемом уравнения не может быть равным нулю'
        if flag:
            a = int(parametr_list['a'])
            b = int(parametr_list['b'])
            c = int(parametr_list['c'])
            D = b*b - 4*a*c
            new_list['d'] = "Дискриминант: " + str(D)
            if D < 0:
                new_list['d_error'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif D == 0:
                x1 =(-b)/2.0*a
                new_list['d_error'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = " + str(x1)

            else:
                x1=(-b + math.sqrt(float(D)))/2.0*a
                x2=(-b - math.sqrt(float(D)))/2.0*a
                new_list['d_error'] = 'Квадратное уравнение имеет два действительных корня: x1 = '+str(x1)+", x2 = " +str(x2)
    return new_list