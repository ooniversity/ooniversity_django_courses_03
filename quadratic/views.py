from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    context = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        context['form'] = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            context['disrcim'] = b**2 - 4*a*c
            if context['disrcim'] > 0:
                context['x1'] = float(
                    (-b + context['disrcim']**(1/2.0)) / (2*a))
                context['x2'] = float(
                    (-b - context['disrcim']**(1/2.0)) / (2*a))
            elif int(context['disrcim']) == 0:
                context['x1'] = context[
                    'x2'] = float(-b / (2*a))
    else:
        context['form'] = QuadraticForm()
    return render(request, 'quadratic/results.html', context)
