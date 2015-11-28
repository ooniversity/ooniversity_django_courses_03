from django.shortcuts import get_object_or_404, render
from courses.models import Course

def index(request):
    params={}
    params['courses']= Course.objects.all()
    return render(request, 'index.html', params)
    
def contact(request):
    return render(request, 'contact.html')
    
def student_list(request):
    return render(request, 'student_list.html')
    
def student_detail(request):
    return render(request, 'student_detail.html')
