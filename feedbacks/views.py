from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
