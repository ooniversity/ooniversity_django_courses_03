from django.shortcuts import render
from quadratic import quadratics
def quadratic_results(request):
    parametr_list = request.GET
    quadratics.quadratic(parametr_list)
    return render(request, 'results.html',quadratics.quadratic(parametr_list))