from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import *

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context ['courses_list'] = Course.objects.all()
       return context

def index(request):
    courses_list = Course.objects.all()
    context = {'courses_list': courses_list}
    return render(request,'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
