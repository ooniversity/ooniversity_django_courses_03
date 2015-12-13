from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.contrib import messages

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    exclude = ['create_date']
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], form.cleaned_data['from_email'], (('slash@25.cm'),), fail_silently=False)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return super(FeedbackView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Fill in your suggestions"
        return context
