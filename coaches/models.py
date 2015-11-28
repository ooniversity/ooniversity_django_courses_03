from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=5, choices=[('M', 'Male'), ('F', 'Female')])
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()

    def username(self):
        return self.user.first_name

    def lastname(self):
        return self.user.last_name

    name = property(username)
    surname = property(lastname)

    def __unicode__(self):
        return self.user.username
