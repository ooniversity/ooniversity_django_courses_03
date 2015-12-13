from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('feedback')

    def form_valid(self, form):
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        print form.cleaned_data
        data = form.cleaned_data
        recipient_list = [i[1] for i in settings.ADMINS]
        send_mail(data['subject'], data['message'], data['from_email'], recipient_list, fail_silently=False)
        return super(FeedbackView, self).form_valid(form)
