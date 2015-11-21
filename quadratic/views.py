# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import loader, Context, Template

def get_discr (a, b, c):
    d=b**2-4*a*c
    return d

def validate_parameter(parameter):
    return_value = ""
    if parameter:
        p = parameter.replace("-", "")
        if p.isdigit():
            return_value = int(parameter)
        else:
            return_value = "коэффициент не целое число"
    else:
        return_value="коэффициент не определен"
    return return_value

def render_contex_parameter(input_parameter = "", parameter = ""):
    templ = Template("{{input_parameter}}<p>{{parameter}}</p>")
    cont_param = Context({'parameter': str(parameter), 'input_parameter': input_parameter})
    return templ.render(cont_param)

def quadratic_results(request):

    a = validate_parameter(request.GET['a'])
    b = validate_parameter(request.GET['b'])
    c = validate_parameter(request.GET['c'])

    errors = False

    if isinstance(a, str):
        par_a = render_contex_parameter(request.GET['a'], a)
        errors = True
    elif a == 0:
        a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        par_a = render_contex_parameter(request.GET['a'], a)
        errors = True
    else:
        par_a = a

    if isinstance(b, str):
        par_b = render_contex_parameter(request.GET['b'], b)
        errors = True
    else:
        par_b = b

    if isinstance(c, str):
        par_c = render_contex_parameter(request.GET['c'], c)
        errors = True
    else:
        par_c = c

    print par_a

    par_d = ""
    solution = ""

    if not errors:
        d= get_discr(a,b,c)

        par_d = render_contex_parameter("Дискриминант: %d" % d)

        if d<0:
            solution = render_contex_parameter("Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.")
        elif d==0:
            x1= round(-b/2.0*a, 1)
            #print "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %f" % x1
            solution = render_contex_parameter("Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f" % x1)
        else:
            x1=(-b+d**(1/2.0))/(2*a)
            x2=(-b-d**(1/2.0))/(2*a)
            solution = render_contex_parameter("Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (x1, x2))

    return render(request, 'quadratic/results.html', {'a': par_a, 'b': par_b, 'c': par_c,'d': par_d, 'solution': solution})
