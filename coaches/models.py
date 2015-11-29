from django.db import models
from django.contrib.auth.models import User

#from django.contrib.auth import User

#from students.models import Student
#from django.contrib.auth import User

class Coach(models.Model):
    user=models.OneToOneField(User)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=1,
        choices=(('M', 'Male'),('F', 'Female')))
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    skype=models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __unicode__(self):
        return self.user
