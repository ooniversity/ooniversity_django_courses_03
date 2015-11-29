from django.db import models


# Create your models here.
class Coach(models.Model):
    class Meta():
        db_table = 'coaches'

    user = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    desciption = models.TextField()

    # __unicode__ on Python 2
    def __unicode__(self):
        return self.user

    # __str__ on Python 3
    def __str__(self):
        return self.user
