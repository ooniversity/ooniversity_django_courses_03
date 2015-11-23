# -*- coding: UTF-8 -*-

def quadratic_func(prms_from_get):

    for key, value in prms_from_get.items():

        if key == 'a' and value == '0':
            prms_from_get['a_msg'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        elif value == '':
            prms_from_get[key+'_msg'] = 'коэффициент не определен'
        elif ''.join(x for x in value if x.isdigit()).isdigit() is False:
            prms_from_get[key+'_msg'] = 'коэффициент не целое число'
        else:
            prms_from_get[key+'_msg'] = 'ок'

    if prms_from_get['a_msg'] is 'ок' and \
            prms_from_get['b_msg'] is 'ок' and \
            prms_from_get['c_msg'] is 'ок':

        a = float(prms_from_get['a'])
        b = float(prms_from_get['b'])
        c = float(prms_from_get['c'])

        discr = b**2 - 4 * a * c;

        if discr > 0:
            import math
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            prms_from_get['x1'] = round(x1, 1)
            prms_from_get['x2'] = round(x2, 1)
        elif discr == 0:
            prms_from_get['x'] = -b / (2 * a)
            
        if discr.is_integer():
            prms_from_get['discr'] = int(discr)
        else:
            prms_from_get['discr'] = discr

    return prms_from_get
