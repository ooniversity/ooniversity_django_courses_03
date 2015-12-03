from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    context = {}
    if request.method == 'GET':
        print 'hello'


    if request.GET.get('a') != None:
        # print 'aa'
        form = QuadraticForm(request.GET)
        context['form'] = QuadraticForm(request.GET)
        if form.is_valid():

            if form.clean_a():
                data = form.cleaned_data
                # print data['a']

                context['disrcim'] = data['b']**2 - 4 * data['a'] * data['c']
                # print context['disrcim']
                if context['disrcim'] > 0:
                    context['x1'] = float(
                        (-data['b'] + context['disrcim']**(1 / 2.0)) / (2 * data['a']))
                    context['x2'] = float(
                        (-data['b'] - context['disrcim']**(1 / 2.0)) / (2 * data['a']))
                elif int(context['disrcim']) == 0:
                    context['x1'] = context[
                        'x2'] = float(-data['b'] / (2 * data['a']))

        return render(request, 'quadratic/results.html', context)
    else:
        context['form'] = QuadraticForm()

        return render(request, 'quadratic/results.html', context)
