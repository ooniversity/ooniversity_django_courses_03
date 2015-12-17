from django.shortcuts import render
from courses.models import Course
from django.views.generic.list import ListView

class IndexView(ListView):
    model = Course
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['course'] = Course.objects.all()
        return context


#def index(request):
#    data_course = Course.objects.all()
#    return render(request,'index.html', {'course': data_course})

def contact(request):
    return render(request,'contact.html')

def student_detail(request):
    return render(request,'student_detail.html')

def student_list(request):
    return render(request,'student_list.html')


