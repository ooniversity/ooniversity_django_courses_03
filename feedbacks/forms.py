from django import forms
from feedbacks.models import Feedback


# Create your views here.
class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
