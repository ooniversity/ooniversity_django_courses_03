from django.shortcuts import render
from django.http import HttpResponse

from equation_solver.equation_solver import calculate

def index(request):
	return HttpResponse("Hello world")

def quadratic_results(request):
	params = {}
	params["a"] = request.GET['a']
	params["b"] = request.GET['b']
	params["c"] = request.GET['c']

	# result = calculate(params)

	return render(request, 'results.html', {'params': params})

