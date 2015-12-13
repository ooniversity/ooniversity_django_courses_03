from django.shortcuts import redirect, render
from feedbacks.models import Feedback
from feedbacks import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here.
class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)