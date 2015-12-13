# -*- coding: utf-8 -*-

from django import forms
from feedbacks.models import Feedback
from datetime import datetime


class FeedbackForm(forms.ModelForm):
    # somefield = forms.CharField(
    # widget=forms.TextInput(attrs={'readonly':'readonly'}))

    create_date = forms.DateTimeField(initial=datetime.now,
                                      widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))

    from_email = forms.EmailField(initial='s.pod.pub@ya.ru',
                                  widget=forms.EmailField(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Feedback
        fields = '__all__'
