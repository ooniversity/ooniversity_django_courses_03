from django.shortcuts import render
from courses.models import Course


def index(request):
    return render(request, 'index.html', { 'courses': Course.objects.all()})

def contact(request):
	return render(request, 'contact.html')