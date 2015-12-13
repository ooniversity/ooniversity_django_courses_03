from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=50)  
    subject = models.CharField(max_length=500)
    message = models.TextField()           
    from_email = models.EmailField(max_length = 50)
    create_date = models.DateTimeField(auto_now=True, auto_now_add=True)

