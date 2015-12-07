from django.shortcuts import render
from courses.models import Course


def index(request):
    list_courses = Course.objects.all().order_by('name')
    context = {
        'list_courses': list_courses,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
