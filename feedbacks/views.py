from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


# Create your views here.
class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'

    def form_valid(self, form):
        feedback = form.save()
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form)
