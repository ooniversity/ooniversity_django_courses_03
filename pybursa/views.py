from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound
from courses.models import *


# Create your views here.
def index(request):
    result = { 'courses': Course.objects.all()}
    return render(request, 'index.html', result)


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')

def base(request):
    return render(request, 'base.html')
