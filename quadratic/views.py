from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from quadratic import forms


def quadratic_results(request):
    d = None
    form = forms.QuadraticForm()
    if request.method == "GET":
        form = forms.QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            

            if int(a) != 0:
                d = int(b) ** 2 - 4 * int(a) * int(c)
            else:
                d = None

    var_x = ''
    var_x1 = ''
    var_x2 = ''

    if d < 0:
        var_x1 = ''
        var_x2 = ''
        
    elif d == 0:
        var_x = -int(b) / 2 * int(a)
        var_x = float(var_x)

    elif d > 0:
        b = int(b)
        a = int(a)
        var_x1 = (-b + d ** (1 / 2.0)) / (2 * a)
        var_x1 = round(var_x1, 1)
        var_x2 = (-b - d ** (1 / 2.0)) / (2 * a)
        var_x2 = round(var_x2, 1)

    
    sl_full = {'discr': d, 'x': var_x, 'x1': var_x1, 'x2': var_x2, }
    sl_full['form'] = form
    return render(request, 'quadratic/results.html', sl_full)
=======

def quadratic_results(request, a, b, c):
    var_a = 'a'
    var_b = 'b'
    var_c = 'c'
    d = var_b ** 2 - 4 * var_a * var_c
    
    sl_full2 = {'sl_full': d, 'a': var_a, 'c': var_b, 'a': var_b}
    return render(request, 'results.html', sl_full2)

>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
