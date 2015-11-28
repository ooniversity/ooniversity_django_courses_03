from django.db import models
from courses.models import Course

class Student(models.Model):
    """Student class"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    short_description = models.CharField(max_length=255)
    description =  models.TextField()

    def __unicode__(self):
        return self.name
