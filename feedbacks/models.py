from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=120)
	from_email = models.EmailField()
	message = models.TextField()
	create_date = models.DateTimeField(auto_now=True)