from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        mail_admins(self.object.subject, self.object.message)
        return super(FeedbackView, self).form_valid(form)
