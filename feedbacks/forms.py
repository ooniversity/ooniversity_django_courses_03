# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from feedbacks.models import Feedback
import datetime
from django.utils import timezone

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
	#def __init__(self, args, *kwargs):
		#super(FeedbackForm, self).__init__(*args, **kwargs)
		#elf.initial['create_date'] = datetime.datetime.now()
