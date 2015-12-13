# -*- coding:UTF-8 -*-
from django import forms
from feedbacks.models import *

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'
