from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse,  reverse_lazy

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
    return render(request,'404.html')

def error_handler500(request):
    return render(request,'500.html')
