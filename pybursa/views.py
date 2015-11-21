from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def student_list(request):
    return render(request, 'student_list.html')
def student_detail(request):
    return render(request, 'student_detail.html')
#add comment smth wrong happened