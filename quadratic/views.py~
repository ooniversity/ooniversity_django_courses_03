from django.shortcuts import render
from quadratic.models import QuadraticEquation

def quadratic_results(request):
    equation = {}
    equation['a'] = request.GET.get('a', '')
    equation['b'] = request.GET.get('b', '')
    equation['c'] = request.GET.get('c', '')
    
    equation = QuadraticEquation(equation)
    
    params = {}
    params['a'] = equation.data['a']
    params['b'] = equation.data['b']
    params['c'] = equation.data['c']
   
    params['has_error'] = equation.has_error
    
    params['a_error'] = equation.errors.get('a', None)
    params['b_error'] = equation.errors.get('b', None)
    params['c_error'] = equation.errors.get('c', None)
    
    params['d'] = equation.data.get('d', None)
    params['description'] = equation.result.get('description', None)
    params['x1'] = equation.result.get('x1', None)
    params['x2'] = equation.result.get('x2', None)
    
    
    return render(request, 'quadratic/results.html', params)
    
  
