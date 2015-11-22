## -*- coding: utf-8 -*-
## coding: utf8
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpRequest

def quadratic_results(request):
    context = {}
    flag_calculate_D = {'a':True, 'b':True, 'c':True}
    print flag_calculate_D
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

    if a == None:
        context['a'] = 'коэффициент не определен'
        flag_calculate_D['a'] = False
    elif not a.isdigit():
        context['a'] = 'коэффициент не целое число'
        flag_calculate_D['a'] = False
    elif int(a) == 0:
        context['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        flag_calculate_D['a'] = False
    else:
        context['a'] = int(a)

    if b == None:
        context['b'] = 'коэффициент не определен'
        flag_calculate_D['b'] = False
    elif not b.isdigit():
        context['b'] = 'коэффициент не целое число'
        flag_calculate_D['b'] = False
    else:
        context['b'] = int(b)

    if c == None:
        context['c'] = 'коэффициент не определен'
        flag_calculate_D['c'] = False
    elif not c.isdigit():
        context['c'] = 'коэффициент не целое число'
        flag_calculate_D['c'] = False
    else:
        context['c'] = int(c)
    print flag_calculate_D
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
                                  'x1 = x2 = %f') % x
        else:
            context['D'] = D
            x1 = -context['b'] + D / (2 * context['a'])
            x2 = -context['b'] + D / (2 * context['a'])
            context['solution'] =('Квадратное уравнение имеет два действительных корня: x1 = %f, x2 = %f') % (x1, x2)
    return render(request, 'results.html', context)

# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})