# -*- coding:UTF-8 -*-

from django.shortcuts import get_object_or_404, render
from courses.models import Course
# from students.models import Student
# from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})


def contact(request):
    return render(request, 'contact.html')


'''
def contact(request):
   return render(request, 'contact.html')

# implemented short record in urls.py

class ContactView(TemplateView):
   template_name = 'contact.html'


def list_view(request):
    return render(request, 'list.html', {'students': Student.objects.all()})

def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
'''

