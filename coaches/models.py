from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=2, choices=(('M', 'Male'),('F', 'Female')), default='M')
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    description = models.TextField()
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user.username