from django.views.generic import TemplateView
import datetime
from courses.models import Course


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


'''
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html',
                  {'courses':courses,
                   })

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')
	
def student_detail(request):
	return render(request, 'student_detail.html')
'''

