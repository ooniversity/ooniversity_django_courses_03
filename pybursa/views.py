from django.shortcuts import render, render_to_response
from django.template import RequestContext
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
#    return render(request, 'index.html', {'course': data_course})

def contact(request):
    return render(request,'contact.html')

def student_detail(request):
    return render(request,'student_detail.html')

def student_list(request):
    return render(request,'student_list.html')

'''
def my_error_404(request):
    return render(request, '404.html', {'message': 'Sorry, page is not found'})

def my_error_500(request):
    return render(request, '500.html', {'message': 'Sorry, internal server error occurred'})
'''

def my_error_404(request):
    response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' },
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def my_error_500(request):
    response = render_to_response('500.html', { 'message' : 'Sorry, internal server error occurred' },
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

