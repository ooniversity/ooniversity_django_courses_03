# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import QuadraticForm


def quadratic_results(request):
    data = {}
    if request.GET.get('a') is None and request.GET.get('b') is None and request.GET.get('c') is None:
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.GET)

    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']

        d = pow(b, 2) - 4 * a * c

        data['print_d'] = "Дискриминант: %(d)d" % {'d': d}
        if d < 0:
            data['d_out'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        if d == 0:
            x = -int(b) / 2 * int(a)
            data['d_out'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:" \
                            " x1 = x2 = %s" % float(x)
        if d > 0:
            x1 = (-int(b) + d ** (1 / 2.0)) / 2 * int(a)
            x2 = (-int(b) - d ** (1 / 2.0)) / 2 * int(a)
            data['d_out'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (
                float(x1), float(x2))

    data['form'] = form
    return render(request, "results.html", data)
