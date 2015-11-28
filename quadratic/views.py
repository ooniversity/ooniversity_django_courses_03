#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader


def quadratic_results(request):
    # data = {'a' : request.GET['a'], 'b' : request.GET['b'], 'c' : request.GET['c'] };
    error = ''

    discr = ''
    title = u'Квадратное уравнение a*x*x + b*x +c = 0'

    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    x1 = ''
    x2 = ''
    res = ''

    data = {
        'a' : {'val': a, 'err' : ''},
        'b' : {'val': b, 'err' : ''},
        'c' : {'val': c, 'err' : ''}
    }

    for key,row in data.iteritems():
        if row['val'] == '':
            data[key]['err'] = u'коэффициент не определен'
        if key == 'a' and row['val'] == '0':
            data[key]['err'] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        if row['val'].isalpha():
            data[key]['err'] = u'коэффициент не целое число'


    if len(a) > 0 and len(b) > 0 and len(c) > 0  and int(a) != 0  and not a.isalpha() and not b.isalpha() and not c.isalpha():
        d = int(b) ** 2 - 4 * int(a) * int(c)
        discr = u'Дискриминант: '+str(d)
        if d >= 0:
            import math
            dd = math.sqrt(d)
            x1 = ( -float(b) + float(dd) ) / (float(a) * 2)
            x2 = ( -float(b) - float(dd) ) / (float(a) * 2)

            x1 = round(x1, 1)
            x2 = round(x2, 1)

            if x1 != x2 :
                res = u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (str(x1), str(x2))
            else:
                res = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % str(x1)
        else:
            res = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'


    template = loader.get_template('results.html')
    context = RequestContext(request, {
        'data': data,
        'error': error,
        'discr': discr,
        'title': title,
        'x1': x1,
        'x2': x2,
        'res': res,

    })
    return HttpResponse(template.render(context))