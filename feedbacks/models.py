from django.db import models
import datetime

class Feedback(models.Model):
    name = models.CharField( max_length=225)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
		return self.name
 
