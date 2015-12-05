from django.db import models
from django.contrib.auth.models import User

class Coach (models.Model):
    user = models.OneToOneField (User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices = (('M','Male'), ('F','Female')))
    description = models.TextField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=30)
    def  __unicode__(self):
        return self.user.username
    def Surname(self):
        return self.user.last_name
    last_name = property(Surname)
    def Name(self):
        return self.user.first_name
    first_name = property(Name)
    def Email(self):
        return self.user.email
    email = property(Email)
