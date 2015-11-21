from django.shortcuts import render


def quadratic_results(request):
    content = {}
    for key in request.GET.keys():
        try:
            content[key] = int(request.GET[key])
            content[key + '_type'] = 'integer'
        except ValueError:
            if request.GET[key] == '':
                content[key] = ''
            else:
                content[key] = str(request.GET[key])
            content[key + '_type'] = 'string'

    a = content['a']
    b = content['b']
    c = content['c']

    if all(map(lambda x: isinstance(x, int), (a, b, c))) and a != 0:
        content['square'] = b**2 - 4 * a * c
        if content['square'] > 0:
            content['x1'] = float((-b + content['square']**(1 / 2.0)) / (2 * a))
            content['x2'] = float((-b - content['square']**(1 / 2.0)) / (2 * a))
        elif content['square'] == 0:
            content['x1'] = content['x2'] = float(-b / (2 * a))
    else:
        content['square'] = ''

    return render(request, 'quadratic/results.html', content)
