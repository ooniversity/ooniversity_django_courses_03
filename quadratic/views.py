# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.template import loader, Context, Template
from quadratic.forms import QuadraticForm


def get_discr (a, b, c):
    d=b**2-4*a*c
    return d

def quadratic_results(request):

    contex = {}
    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            contex['a'] = a
            contex['b'] = b
            contex['c'] = c

            par_d = ""
            solution = ""

            d = get_discr(a,b,c)
            par_d = "Дискриминант: %d" %d

            if d<0:
                solution = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d==0:
                x1= round(-b/2.0*a, 1)
                solution = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f" % x1
            else:
                x1=(-b+d**(1/2.0))/(2*a)
                x2=(-b-d**(1/2.0))/(2*a)
                solution = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (x1, x2)
            contex['d'] = par_d
            contex['solution'] = solution
    else:
        form = QuadraticForm()

    contex['form'] = form

    return render(request, 'quadratic/results.html', contex)
