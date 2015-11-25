from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from courses.models import Course

def index(request):
    args={}
    args['courses'] = Course.objects.all()

    return render(request, 'index.html', args)
def contact(request):
    return render(request, 'contact.html')
def student_list(request):
    return render(request, 'student_list.html')
def student_detail(request):
    return render(request, 'student_detail.html')            
    