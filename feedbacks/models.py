from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
