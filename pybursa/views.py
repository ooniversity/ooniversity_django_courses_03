from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course
from coaches.models import Coach


def index(request):
    
    list_of_courses = Course.objects.all()
    list_of_coachers = Coach.objects.all()

    return render(request, 'index.html', {
        "list_of_courses": list_of_courses,
        "coaches": list_of_coachers,
        })

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
