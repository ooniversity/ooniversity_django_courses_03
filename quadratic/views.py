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
            #a = int(request.GET['a'])
            #b = int(request.GET['b'])
            #c = int(request.GET['c'])
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            contex['a'] = a
            contex['b'] = b
            contex['c'] = c

            par_d = ""
            solution = ""

                #if not a_error and not b_error and not c_error:
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
    print contex

    """
        errors = False
        a = request.GET['a']
        a_error = ""
        if a:
            p = a.replace("-", "")
            if p.isdigit():
                if a == "0":
                    a_error = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
                else:
                    a = int(a)
            else:
                a_error = "коэффициент не целое число"
        else:
            a_error="коэффициент не определен"
        b = request.GET['b']
        b_error = ""
        if b:
            p = b.replace("-", "")
            if p.isdigit():
                b = int(b)
            else:
                b_error = "коэффициент не целое число"
        else:
            b_error="коэффициент не определен"
        c = request.GET['c']
        c_error = ""
        if c:
            p = c.replace("-", "")
            if p.isdigit():
                c = int(c)
            else:
                c_error = "коэффициент не целое число"
        else:
            c_error="коэффициент не определен"
        par_d = ""
        solution = ""
        if not a_error and not b_error and not c_error:
            d = get_discr(a,b,c)
            par_d = "Дискриминант: %d" %d
            if d<0:
                solution = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d==0:
                x1= round(-b/2.0*a, 1)
                #print "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %f" % x1
                solution = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f" % x1
            else:
                x1=(-b+d**(1/2.0))/(2*a)
                x2=(-b-d**(1/2.0))/(2*a)
                solution = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (x1, x2)
        return render(request, 'quadratic/results.html', {'a': a, 'a_error': a_error, 'b': b, 'b_error': b_error, 'c': c,
            'c_error': c_error,'d': par_d, 'solution': solution, 'form': form})
    """

    #return render(request, 'quadratic/results.html', {'a': a, 'b': b, 'c': c,
                          # 'd': par_d, 'solution': solution, 'form': form})


    return render(request, 'quadratic/results.html', contex)
