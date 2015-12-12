from feedbacks.models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		exclude = ['create_date']
		fields = '__all__'