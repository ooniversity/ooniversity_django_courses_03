from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from feedbacks.forms import FeedbackForm
from django.core.urlresolvers import reverse_lazy


class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = "feedback.html"
    success_url = reverse_lazy("feedback")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)