from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    
    def form_valid(self, form):
        feedback = form.save()
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form)
    

