from django.db import models


# Feedback
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
