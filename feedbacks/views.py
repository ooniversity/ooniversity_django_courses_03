from django.contrib import messages
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback

# Create your views here.
class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback/feedback.html"
	success_url = reverse_lazy('feedback')

	def form_valid(self, form):
		self.object = form.save()
		message = 'Thank you for your feedback! We will keep in touch with you very soon!'
		messages.success(self.request, message)
		mail_admins(self.object.subject, self.object.message)
		return super(FeedbackView, self).form_valid(form)