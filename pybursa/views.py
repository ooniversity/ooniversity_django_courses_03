from django.shortcuts import render
from courses.models import Course

courses = Course.objects.all()
def index(request):
    return render(request, 'index.html', 
    	{'courses': courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

