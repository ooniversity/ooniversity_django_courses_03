from django.shortcuts import render

def get_discriminant(request, a, b, c):
	res = pow(b, 2.0) - 4 * a * c
	return res

def quadratic_results(request, a, b, c):
	if get_diskriminant < 0:
		res = render(request, 'results.html', {'a':a, 'b':b, 'c':c})
