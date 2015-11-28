from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson
from students.models import Student



def index(request):
    return render(request, 'index.html', {'courses':Course.objects.all()})

'''
def index(request):
    return render(request, 'index.html')
'''

def contact(request):
    return render(request, 'contact.html')


def list_view(request):
    return render(request, 'list.html', {'students':Student.objects.all()})



def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')