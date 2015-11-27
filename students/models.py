from django.db import models
# Create your models here.
from courses.models import Course
#import courses.models

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

