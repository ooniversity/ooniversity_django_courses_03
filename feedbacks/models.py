from django.db import models


class Feedback (models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField(max_length=255)
    create_date = models.DateField(auto_now=True, auto_now_add=True)

