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

"""
class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        send_mail(
            subject=form.cleaned_data.get('subject'),#.encode('utf-8').strip(),
            message=form.cleaned_data.get('message'),
            from_email=form.cleaned_data.get('mesfrom_emailsage'),
            recipient_list=settings.ADMINS
        )
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!', extra_tags='msg')
        return super(FeedbackView, self).form_valid(form)
"""
