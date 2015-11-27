from django.db import models


class Coach(models.Model):
    # user = models.OneToOneField(User)      ????
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=255, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=30)
    description = models.TextField()


gender = models.IntegerField(default=1, choices=((1, 'Male'), (2, 'Female')))
