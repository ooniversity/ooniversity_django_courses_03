from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        message = super(FeedbackView, self).form_valid(form)
        mes = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, mes)
        mail_admins(self.object.subject, self.object.message)
        return message

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context
