# -*- coding:UTF-8 -*-
from django import forms
from django.db import models

class Feedback(models.Model):
    """Feedback class"""
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    from_email =  models.EmailField()
    create_date = forms.DateTimeField(widget = forms.TextInput(
        attrs={'readonly':'readonly'}))

    def __unicode__(self):
        return self.name
