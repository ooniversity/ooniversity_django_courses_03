#-*-coding: utf-8-*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
import models
import datetime
from forms import *

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    success_url = reverse_lazy('feedback')
    def form_valid(self, form):
        messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
        form.create_date = datetime.datetime.now()
        return super(FeedbackView, self).form_valid(form)
