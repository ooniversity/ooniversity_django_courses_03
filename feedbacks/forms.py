from django.forms import ModelForm
from feedbacks.models import Feedback


class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback

