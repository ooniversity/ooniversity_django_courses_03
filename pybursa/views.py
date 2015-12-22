from django.shortcuts import get_object_or_404, render
from courses.models import Course

def index(request):
    params={}
    params['courses']= Course.objects.all()
    return render(request, 'index.html', params)

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def not_found(request):
    response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' },
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def server_error(request):
    response = render_to_response('500.html', { 'message' : 'Sorry, internal server error occurred' },
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
