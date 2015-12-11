from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins
import datetime
from django.conf import settings


# class FeedbackView(CreateView):
#     model = Feedback
#     form_class = FeedbackForm
#     template_name = "feedback.html"
#     success_url = reverse_lazy('feedback')
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         mail_admins(data['subject'], data['message'], fail_silently=True)
#         messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!',
#                          extra_tags='msg')
#         return super(FeedbackView, self).form_valid(form)


class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        message = super(FeedbackView, self).form_valid(form)
        mes = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, mes)
        mail_admins(self.object.subject, self.object.message)
        return message

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context
