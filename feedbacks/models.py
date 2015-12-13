from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    message = models.TextField(blank = True)
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
    	return self.name
