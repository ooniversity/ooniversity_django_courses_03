from django.shortcuts import render
from courses.models import Course
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

# def contact(request):
#     return render(request, 'contact.html')


# def student_list(request):
#    return render(request, 'student_list.html')


# def student_detail(request):
#     return render(request, 'student_detail.html')
