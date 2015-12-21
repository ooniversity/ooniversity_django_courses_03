from django.shortcuts import render, render_to_response
from django.template import RequestContext
from courses.models import Course

def index(request):
    gcourses = Course.objects.all()
    return render(request,'index.html', {'gc': gcourses})
    
def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

