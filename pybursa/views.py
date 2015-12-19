from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse,  reverse_lazy
from django.template import RequestContext

from polls.models import Choice, Question
from courses.models import Course
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.conf import settings
from django.core.mail import send_mail

def index(request):

    return render(request, 'index.html', {'courses_all':Course.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def error_handler404(request):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response
    #return render(request,'404.html')

def error_handler500(request):
    response = render_to_response('500.html', context_instance=RequestContext(request))
    response.status_code = 500
    return response
    #return render(request,'500.html')
