from django.shortcuts import render


def quadratic_results(request):
    return render(request, 'quadratic/result.html')
