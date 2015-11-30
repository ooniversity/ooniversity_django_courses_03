from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)  
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 1, choices = (('M','Male'), ('F','Female')))
    phone = models.CharField(max_length = 20)       
    address = models.CharField(max_length = 254)    
    skype = models.CharField(max_length = 100)      
    description = models.TextField()                

    def __unicode__(self):
        return self.user.username

    