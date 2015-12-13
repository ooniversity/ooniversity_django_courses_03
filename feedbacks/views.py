from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.core.mail import mail_admins

# Create your views here.
class FeedbackView(CreateView):

    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')
    context_object_name = 'feedback'


    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context

    def form_valid(self, form):
        feedback_message = form.save()
        message = 'Thank you for your feedback! We will keep in touch with you very soon!'
        messages.success(self.request, message)
        mail_admins(feedback_message.subject, feedback_message.message)
        return super(FeedbackView, self).form_valid(form)