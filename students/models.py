from django.db import models
from courses.models import Course


# Create your models here.
class Student(models.Model):
    # class Meta():
    #    db_table = 'student'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    # __unicode__ on Python 2
    def __unicode__(self):
        return self.name

    # __str__ on Python 3
    def __str__(self):
        return self.name

