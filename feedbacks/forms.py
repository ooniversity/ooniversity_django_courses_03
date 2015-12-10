from django import forms
from django.forms import ModelForm
from feedbacks.models import Feedback
import datetime

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.initial['create_date'] = datetime.datetime.now()
