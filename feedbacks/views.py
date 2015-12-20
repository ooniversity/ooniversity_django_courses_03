# -*- coding:UTF-8 -*-

from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy, reverse
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.conf import settings


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedbaSck')

# send_mail(
    # subject, message, from_email, recipient_list, fail_silently=False,
    #  auth_user=None, auth_password=None, connection=None, html_message=None)

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        recipient_list = settings.ADMINS
        send_mail(subject, message, from_email, recipient_list)
        message = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = u'Leave feedback'
        return context
