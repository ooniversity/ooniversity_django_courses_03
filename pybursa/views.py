
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
