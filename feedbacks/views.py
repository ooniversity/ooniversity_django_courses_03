from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from feedbacks.models import Feedback 
from feedbacks.forms import FeedbackForm 
from django.core.mail import mail_admins

class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback.html" 
	#success_url = reverse_lazy('index')
	def form_valid(self, form):
		mail_admins(form.cleaned_data.get('subject'),form.cleaned_data.get('message'),fail_silently=True)
		success_mes = 'Thank you for your feedback! We will keep in touch with you very soon!'
		messages.success(self.request, success_mes, extra_tags='msg')
		return super(FeedbackView, self).form_valid(form)	
