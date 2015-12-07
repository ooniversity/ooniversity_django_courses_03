from django.shortcuts import render_to_response
from courses.models import Course


def index(request):
    list_courses = Course.objects.all().order_by('name')
    context = {
        'list_courses': list_courses,
    }
    return render_to_response('index.html', context)


def contact(request):
    return render_to_response('contact.html')
