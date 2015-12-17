from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from courses.models import Course

def index(request):
    return render(request, 'index.html', {'courses_list': Course.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
=======
from courses.models import Course

def index (request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def student_list(request):
    return render(request, 'student_list.html', {})

def student_detail(request):
    return render(request, 'student_detail.html', {}) 

>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
