from django.views.generic.edit import CreateView
from feedbacks import models
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = models.Feedback
    success_url = reverse_lazy('feedback')
    template_name = 'feedback.html'

    def form_valid(self, form):
        feedback = form.save()
        message_string = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message_string)
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form)