from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

# __unicode__ on Python 2
    def __unicode__(self):
        return self.subject

    # __str__ on Python 3
    def __str__(self):
        return self.subject
