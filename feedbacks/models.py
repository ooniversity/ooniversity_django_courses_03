# -*- coding:UTF-8 -*-
from django.utils import timezone
from django import forms
from django.db import models


class Feedback(models.Model):
    """Feedback class"""
    name = models.CharField('Your name', max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    from_email =  models.EmailField('Your e-mail')
    create_date = models.DateTimeField(auto_now_add=True, default=timezone.now())

    def __unicode__(self):
        return self.name
