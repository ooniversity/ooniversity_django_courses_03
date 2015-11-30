from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    """Coach class"""
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')))
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
    def get_name(self):
        return self.user.first_name
    def get_surname(self):
        return self.user.last_name
    def get_is_stuff(self):
        return self.user.first_name
    def get_email(self):
        return self.user.email
    def __unicode__(self):
        return self.user.username
