from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    
    success_url = reverse_lazy('feedback')
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        mail_admins(self.object.subject, self.object.message)
        context = super(FeedbackView, self).form_valid(form)
        message = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return context

