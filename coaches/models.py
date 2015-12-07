from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, default='M', choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def is_staff(self):
        return self.user.is_staff


