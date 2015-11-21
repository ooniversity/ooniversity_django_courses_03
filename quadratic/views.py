from django.shortcuts import render


def quadratic_results(request):
    value = {}
    for key in request.GET.keys():
        try:
            value[key] = int(request.GET[key])
            value[key + '_type'] = 'integer'
        except ValueError:
            if request.GET[key] == '':
                value[key] = ''
            else:
                value[key] = str(request.GET[key])
            value[key + '_type'] = 'string'

    a = value['a']
    b = value['b']
    c = value['c']

    if all(map(lambda x: isinstance(x, int), (a, b, c))) and a != 0:
        value['disrcim'] = b**2 - 4 * a * c
        if value['disrcim'] > 0:
            value['x1'] = float((-b + value['disrcim']**(1 / 2.0)) / (2 * a))
            value['x2'] = float((-b - value['disrcim']**(1 / 2.0)) / (2 * a))
        elif value['disrcim'] == 0:
            value['x1'] = value['x2'] = float(-b / (2 * a))
    else:
        value['disrcim'] = ''

    return render(request, 'quadratic/results.html', value)
