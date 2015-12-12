from django.db import models
from django.utils import timezone


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(default=timezone.now)

