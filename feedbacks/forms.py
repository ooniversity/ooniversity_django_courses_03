# -*- coding: utf-8 -*-


""" Insert your description
"""


from feedbacks.models import Feedback
from django.forms.models import ModelForm


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
