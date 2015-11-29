from django.shortcuts import render
from courses.models import *

def index(request):
    courses_list = Course.objects.all()
    context = {'courses_list': courses_list}
    return render(request,'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
