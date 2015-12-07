from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user=models.OneToOneField(User)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=255,
        choices=(('M', 'Male'),('F', 'Female')))
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    skype=models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    def get_name(self):
        return self.user.first_name

    def get_surname(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email

    def get_is_staff(self):
        return self.is_staff

    def __unicode__(self):
        return self.user.first_name
