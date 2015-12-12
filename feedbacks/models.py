# -*- coding: utf-8 -*-
from django.db import models
from django import forms


class Feedback(models.Model):
    name = models.CharField(max_length=70)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
