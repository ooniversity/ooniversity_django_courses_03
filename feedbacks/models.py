from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = 
