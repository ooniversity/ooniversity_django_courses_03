from django.shortcuts import render
from courses.models import Course
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
    
'''
def index(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {'courses': courses})
'''	


