from django.contrib import messages
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback


class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback')
    template_name = 'feedbacks/feedback.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Form feedback"
        return context

    def form_valid(self, form):
        feedback = form.save()
        messages.success(
            self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form)
