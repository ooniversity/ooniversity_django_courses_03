from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.contrib import messages

from courses.models import Course


def index(request):
    gcourses = Course.objects.all()
    return render(request,'index.html', {'gc': gcourses})

def contact(request):
    return render(request,'contact.html')

def student_list(request):
    return render(request,'student_list.html')

def student_detail(request):
    return render(request,'student_detail.html')

