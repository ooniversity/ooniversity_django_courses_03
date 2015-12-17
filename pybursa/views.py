from django.shortcuts import render
from courses.models import Course
from django.views.generic import TemplateView

courses = Course.objects.all()
def index(request):
    return render(request, 'index.html', 
    	{'courses': courses})

class ContactView(TemplateView):
	template_name = "contact.html"
