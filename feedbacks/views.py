from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
import datetime
from django.conf import settings 


class FeedbackView(CreateView):
	model = Feedback
	form_class = FeedbackForm
	template_name = "feedback.html"
	success_url = reverse_lazy('feedback')

	def form_valid(self, form):
		send_mail(
			subject=form.cleaned_data.get('subject'),#.encode('utf-8').strip(),
			message=form.cleaned_data.get('message'),
			from_email=form.cleaned_data.get('mesfrom_emailsage'),
			recipient_list=settings.ADMINS
		)
		messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!', extra_tags='msg')
		return super(FeedbackView, self).form_valid(form)

"""
class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedbacks/feedback.html'
	success_url = reverse_lazy('feedbacks:feedback')
	#def get_context_data(self, **kwargs):
		#context = super(StudentCreateView, self).get_context_data(**kwargs)
		#context['title'] = "Student registration"
 		#return context
	def form_valid(self, form):
		added_feedback = form.save()
		success_mes = "Thank you for your feedback! We will keep in touch with you very soon!"
		messages.success(self.request, success_mes, extra_tags='msg')
		return super(FeedbackView, self).form_valid(form)
"""

