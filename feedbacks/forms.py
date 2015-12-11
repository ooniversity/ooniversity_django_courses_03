# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from feedbacks.models import Feedback
import datetime
from django.utils import timezone


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
