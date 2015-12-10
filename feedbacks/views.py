from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.contrib import messages

from feedbacks.models import Feedback


class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('index')
    template_name = 'feedback.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Form feedback"
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        send_mail(data['name'], data['subject'], data['message'],
                  data['from_email'], ['tom@example.com'], fail_silently=False)

        messages.success(self.request, 'Message was sent')
        return super(FeedbackView, self).form_valid(form)
