from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from courses.models import Course


# Create your views here.
#def index_courses(request):
    #courses_list = Course.objects.all()
    #context = {'courses_list': courses_list}
    #return render(request, 'index.html', context)
    #return render(request, 'index.html', {'courses_list': Course.objects.all()})

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'