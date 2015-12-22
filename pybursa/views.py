from django.shortcuts import render # render_to_response
# from django.http import HttpResponse
from courses.models import *
# from django.template import RequestContext, Context, loader


def index(request):
    result = {'courses': Course.objects.all()}
    return render(request, 'index.html', result)


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')

'''
def my_handler404(request):
    template = loader.get_template('404.html')
    context = Context({'message': 'Sorry, page is not found'})
    return HttpResponse(content=template.render(context), status=404)


def my_handler500(request):
    template = loader.get_template('500.html')
    context = Context({'message': 'Sorry, internal server error occurred'})
    return HttpResponse(content=template.render(context), status=404)



def my_handler404(request):
    response = render_to_response('404.html', {'message': 'Sorry, page is not found'},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def my_handler500(request):
    response = render_to_response('500.html', {'message': 'Sorry, internal server error occurred'},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
'''