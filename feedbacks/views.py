from django.shortcuts import redirect, render
from feedbacks.models import Feedback
from feedbacks import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


# Create your views here.
class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        data = form.cleaned_data
        #send_mail(data['subject'], data['message'], data['from_email'], ['golv1974@gmail.com'])
        mail_admins(data['subject'], data['message'], fail_silently=False, connection=None, html_message=None)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)
