from django.shortcuts import render


def quadratic_results(request):
    context = {}
    for key in request.GET.keys():
        try:
            context[key] = int(request.GET[key])
            context[key + '_type'] = 'integer'
        except ValueError:
            if not isinstance(request.GET[key], str):
                context[key] = ''
            else:
                context[key] = str(request.GET[key])
            context[key + '_type'] = 'string'

    a = context['a']
    b = context['b']
    c = context['c']

    if map(lambda x: isinstance(x, int), (a, b, c)) and a != 0:
        context['square'] = b**2 - 4 * a * c
        if context['square'] > 0:
            context['x1'] = float((-b + context['square']**(1 / 2.0)) / (2 * a))
            context['x2'] = float((-b - context['square']**(1 / 2.0)) / (2 * a))
        elif context['square'] == 0:
            context['x1'] = context['x2'] = float(-b / (2 * a))
    else:
        context['square'] = ''

    return render(request, 'quadratic/results.html', context)
