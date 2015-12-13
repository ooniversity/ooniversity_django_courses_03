from django.shortcuts import render
from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm

class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    exclude = ['create_date']
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Leave a feedback"
        return context

    def form_valid(self, form):
        mail_admins(form.cleaned_data['subject']
                         , form.cleaned_data['message'])
        return super(FeedbackView, self).form_valid(form)

'''
    def form_valid(self, form):
        data = form.cleaned_data
        mail_admins(data['subject'], data['message'])
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        self.success_url = reverse_lazy('feedback')
        return super(FeedbackView, self).form_valid(form)
'''
