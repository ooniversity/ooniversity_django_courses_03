# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from feedbacks.models import Feedback
#from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins, send_mail


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    #success_url = reverse_lazy('feedback')
    def form_valid(self, form):
        data = form.cleaned_data
        feedback = form.save()
        mail_admins(data['subject'], data['message'])
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)