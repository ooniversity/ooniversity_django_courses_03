from django.shortcuts import render

def quadratic_results(request, a, b, c):
    var_a = 'a'
    var_b = 'b'
    var_c = 'c'
    d = var_b ** 2 - 4 * var_a * var_c
    
    sl_full2 = {'sl_full': d, 'a': var_a, 'c': var_b, 'a': var_b}
    return render(request, 'results.html', sl_full2)

