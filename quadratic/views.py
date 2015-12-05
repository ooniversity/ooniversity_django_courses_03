## -*- coding: utf-8 -*-
## coding: utf8
from django.shortcuts import render, get_object_or_404
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    global context
    global flag_calculate_D
    context = {}
    form = QuadraticForm(request.GET)
    context['form'] = form
    flag_calculate_D = {'a':True, 'b':True, 'c':True}


    if form.is_valid():
        context['calculate_Done'] = True
        a = int(form['a'].value())
        b = int(form['b'].value())
        c = int(form['c'].value())
        D = b ** 2 - 4 * a * c
        if D < 0:
            context['D'] = D
            context['solution'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif D == 0:
            context['D'] = D
            x = -b / (2 * a)
            context['solution'] =('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: '
                                  'x1 = x2 = %.1f') % x
        else:
            context['D'] = D
            x1 = (-b + D ** (1/2.0)) / (2 * a)
            x2 = (-b - D ** (1/2.0)) / (2 * a)
            context['solution'] =('Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f') % (x1, x2)
    return render(request, 'results.html', context)


def is_number(char):
    try:
        int(char)
        return_value = True
    except:
        return_value = False
    return return_value

def check_input(param, param_value, primary = False):
    message = param+'_message'
    if param_value == None or param_value == '':
        context[param] = ''
        context[message] = 'коэффициент не определен'
        flag_calculate_D[param] = False
    elif not is_number(param_value):
        context[param] = param_value
        context[message] = 'коэффициент не целое число'
        flag_calculate_D[param] = False
    elif int(param_value) == 0 and primary == True:
        context[param] = param_value
        context[message] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        flag_calculate_D[param] = False
    else:
        context[param] = int(param_value)