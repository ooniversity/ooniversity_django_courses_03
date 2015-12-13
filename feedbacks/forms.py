from django.forms import ModelForm
from feedbacks import models


class FeedbackForm(ModelForm):
    class Meta:
        model = models.Feedback
