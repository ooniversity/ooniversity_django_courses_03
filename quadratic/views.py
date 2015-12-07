from django.shortcuts import render
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
            # print request.POST

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
        # print "Roots of the equation doesn't exist"
        #exit()
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

    # d = var_a + int(var_b) + int(var_c)

#eq_ans = 'Result {0}'.format(s)
#return HttpResponse(eq_ans)

    #sl_full = {'discr': d, 'a': a, 'b': b, 'c': c, 'x': var_x, 'x1': var_x1, 'x2': var_x2, }
    sl_full = {'discr': d, 'x': var_x, 'x1': var_x1, 'x2': var_x2, }
    sl_full['form'] = form
    return render(request, 'quadratic/results.html', sl_full)