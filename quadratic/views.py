## -*- coding: utf-8 -*-
## coding: utf8
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpRequest

def quadratic_results(request):
    global context
    global flag_calculate_D
    context = {}
    flag_calculate_D = {'a':True, 'b':True, 'c':True}

    try:
        a = request.GET['a']
    except:
        a = None
    try:
        b = request.GET['b']
    except:
        b = None
    try:
        c = request.GET['c']
    except:
        c = None


    # if a == None or a == '':
    #     context['a'] = ''
    #     context['a_message'] = 'коэффициент не определен'
    #     flag_calculate_D['a'] = False
    # elif not is_number(a):
    #     context['a'] = a
    #     context['a_message'] = 'коэффициент не целое число'
    #     flag_calculate_D['a'] = False
    # elif int(a) == 0:
    #     context['a'] = a
    #     context['a_message'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    #     flag_calculate_D['a'] = False
    # else:
    #     context['a'] = int(a)
    check_input('a',a, True)
    check_input('b',b)
    check_input('c',c)

    # if b == None or b == '':
    #     context['b'] = ''
    #     context['b_message'] = 'коэффициент не определен'
    #     flag_calculate_D['b'] = False
    # elif not is_number(b):
    #     context['b'] = b
    #     context['b_message'] = 'коэффициент не целое число'
    #     flag_calculate_D['b'] = False
    # else:
    #     context['b'] = int(b)
    #
    # if c == None or c == '':
    #     context['c'] = ''
    #     context['c_message'] = 'коэффициент не определен'
    #     flag_calculate_D['c'] = False
    # elif not is_number(c):
    #     context['c'] = c
    #     context['c_message'] = 'коэффициент не целое число'
    #     flag_calculate_D['c'] = False
    # else:
    #     context['c'] = int(c)

    if flag_calculate_D['a'] and flag_calculate_D['b'] and flag_calculate_D['c']:
        context['calculate_Done'] = True
        D = context['b'] ** 2 - 4 * context['a'] * context['c']
        if D < 0:
            context['D'] = D
            context['solution'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif D == 0:
            context['D'] = D
            x = -context['b'] / (2 * context['a'])
            context['solution'] =('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: '
                                  'x1 = x2 = %.1f') % x
        else:
            context['D'] = D
            x1 = (-context['b'] + D ** (1/2.0)) / (2 * context['a'])
            x2 = (-context['b'] - D ** (1/2.0)) / (2 * context['a'])
            context['solution'] =('Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f') % (x1, x2)
    return render(request, 'results.html', context)

# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
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