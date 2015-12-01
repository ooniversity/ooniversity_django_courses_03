from django.shortcuts import render

from forms import QuadraticForm


def quadratic_results(request):
    form = QuadraticForm()
    context = {}
    for key in request.GET.keys():
        if request.GET[key] == '':
            context[key] = ''
            context[key + '_type'] = 'string'
        else:
            try:
                context[key] = int(request.GET[key])
                context[key + '_type'] = 'integer'
            except Exception:
                context[key] = str(request.GET[key])
                context[key + '_type'] = 'string'

    a = context['a']
    b = context['b']
    c = context['c']

    if all(map(lambda x: isinstance(x, int), (a, b, c))) and a != 0:
        context['disrcim'] = b**2 - 4 * a * c
        if context['disrcim'] > 0:
            context['x1'] = float(
                (-b + context['disrcim']**(1 / 2.0)) / (2 * a))
            context['x2'] = float(
                (-b - context['disrcim']**(1 / 2.0)) / (2 * a))
        elif context['disrcim'] == 0:
            context['x1'] = context['x2'] = float(-b / (2 * a))
    else:
        context['disrcim'] = ''

    context['form'] = form

    return render(request, 'quadratic/results.html', context)
