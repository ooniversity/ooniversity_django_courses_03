from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 1, choices = (('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length = 15)
    address = models.CharField(max_length = 30)
    skype = models.CharField(max_length = 30)
    description = models.TextField()

    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name

    def __unicode__(self):
        return self.user.username
