from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.name
