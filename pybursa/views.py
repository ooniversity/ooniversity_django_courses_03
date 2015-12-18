from django.shortcuts import render
from courses.models import *

def index(request):
    result = {'courses': Course.objects.all()}
    return render(request, 'index.html', result)

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')