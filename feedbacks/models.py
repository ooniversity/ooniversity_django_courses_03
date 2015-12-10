# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    create_date = models.DateTimeField(default=datetime.datetime.now)
    from_email = models.EmailField()
    
    def __unicode__(self):
        return self.name
    
