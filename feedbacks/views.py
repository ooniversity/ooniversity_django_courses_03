from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.core.mail import mail_admins
from django.contrib import messages

class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback.html"
	form_class = FeedbackForm
	exclude = ['create_date']


	def form_valid(self, form):
		data = form.cleaned_data
		mail_admins(data['subject'], data['message'], fail_silently=True)

		msg = 'Thank you for your feedback! We will keep in touch with you very soon!'

		self.success_url = reverse_lazy('feedback')
		messages.success(self.request, msg)

		return super(FeedbackView, self).form_valid(form)

