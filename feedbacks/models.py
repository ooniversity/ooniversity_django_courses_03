# -*- coding: utf-8 -*-
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    from_email = models.EmailField()

    def __unicode__(self):
        return self.name
