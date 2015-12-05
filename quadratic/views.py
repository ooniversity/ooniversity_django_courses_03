from django.shortcuts import render
from django.http import HttpResponse
import forms


# Create your views here.

#def results(request):
    #return HttpResponse("Hello, it is results - quadratic.")
    #return render(request, 'results.html')

def quadratic_results(request):
    form = forms.QuadraticForm()
    print request.POST
    if request.GET['a']:
        var_a = request.GET['a']
    else:
        var_a = ''
    if request.GET['b']:
        var_b = request.GET['b']
    else:
        var_b = ''
    if request.GET['c']:
        var_c = request.GET['c']
    else:
        var_c = ''
    if (var_a.isdigit() is True and int(var_a) != 0) and var_b.isdigit() is True and var_c.isdigit() is True:
        d = int(var_b) ** 2 - 4 * int(var_a) * int(var_c)
    else:
        d = None

    var_x = ''
    var_x1 = ''
    var_x2 = ''

    if d < 0:
        var_x1 = ''
        var_x2 = ''
        #print "Roots of the equation doesn't exist"
        #exit()
    elif d == 0:
        var_x = -int(var_b) / 2 * int(var_a)
        var_x = float(var_x)

    elif d > 0:
        var_b = int(var_b)
        var_a = int(var_a)
        var_x1 = (-var_b + d ** (1/2.0)) / (2 * var_a)
        var_x1 = round(var_x1, 1)
        var_x2 = (-var_b - d ** (1/2.0)) / (2 * var_a)
        var_x2 = round(var_x2, 1)
    #d = var_a + int(var_b) + int(var_c)
    #eq_ans = 'Result {0}'.format(s)
    #return HttpResponse(eq_ans)

    sl_full = {'discr': d, 'a': var_a, 'b': var_b, 'c': var_c, 'x': var_x, 'x1': var_x1, 'x2': var_x2,}
    sl_full['form'] = form
    return render(request, 'results.html', sl_full)