from django.shortcuts import render
from django.http import HttpResponse
from quadratic.models import QuadraticCalc
from courses.models import Course, Lesson
from students.models import Student

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {"courses": courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def quadratic_results(request):
    initial = {}
    initial['a'] = request.GET.get('a', '')
    initial['b'] = request.GET.get('b', '')
    initial['c'] = request.GET.get('c', '')

    initial = QuadraticCalc(initial)

    variables = {}
    variables['a'] = initial.data['a']
    variables['b'] = initial.data['b']
    variables['c'] = initial.data['c']

    variables['error'] = initial.error

    variables['a_error'] = initial.errors.get('a', None)
    variables['b_error'] = initial.errors.get('b', None)
    variables['c_error'] = initial.errors.get('c', None)


    variables['x1'] = initial.result.get('x1', None)
    variables['x2'] = initial.result.get('x2', None)
    variables['d'] = initial.data.get('d', None)
    variables['description'] = initial.result.get('description', None)

    return render(request, 'results.html', variables)
