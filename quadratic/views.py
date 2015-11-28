from django.shortcuts import render


def quadratic_results(request):
    value = {}
    for key in request.GET.keys():
        if request.GET[key] == '':
            value[key] = ''
            value[key + '_type'] = 'string'
        else:
            try:
                value[key] = int(request.GET[key])
                value[key + '_type'] = 'integer'
            except Exception:
                value[key] = str(request.GET[key])
                value[key + '_type'] = 'string'

    a = value['a']
    b = value['b']
    c = value['c']
