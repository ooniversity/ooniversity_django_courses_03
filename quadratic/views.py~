from django.shortcuts import render


def quadratic_results(request):
    eq = {}
    for item in request.GET.keys():
        if request.GET[item] == '':
            eq[item] = ''
            eq[item + '_unit'] = 'str'
        else:
            try:
                eq[item] = int(request.GET[item])
                eq[item + '_unit'] = 'int'
            except Exception:
                eq[item] = str(request.GET[item])
                eq[item + '_unit'] = 'str'
                

    a = eq['a']
    b = eq['b']
    c = eq['c']

    if all(map(lambda x: isinstance(x, int), (a, b, c))) and a != 0:

        eq['discr'] = b**2 - 4 * a * c
        if eq['discr'] == 0:
            eq['x1'] = eq['x2'] = float(-b / (2 * a))
        elif eq['discr'] > 0:
            eq['x1'] = float((-b + eq['discr']**(1 / 2.0)) / (2 * a))
            eq['x2'] = float((-b - eq['discr']**(1 / 2.0)) / (2 * a))
    else:
        eq['disrcim'] = ''

    return render(request, 'quadratic/results.html', eq)
