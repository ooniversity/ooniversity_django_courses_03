# -*- coding: utf-8 -*-
from django.shortcuts import render
import forms


def quadratic_results(request):
    if request.GET:
        form = forms.QuadraticForm(request.GET)
    else:
        form = forms.QuadraticForm()
    dscrt = x1 = x2 = None
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        dscrt = b**2 - 4*a*c
        if dscrt > 0:
            x1 = float((-b + dscrt**0.5) / (2 * a))
            x2 = float((-b - dscrt**0.5) / (2 * a))
        elif dscrt == 0:
            x1 = x2 = float(-b / (2 * a))
        else:
            x1 = x2 = None

    return render(request, 'quadratic/results.html',
                           {'form': form, 'dscrt': dscrt, 'x1':x1, 'x2': x2})

