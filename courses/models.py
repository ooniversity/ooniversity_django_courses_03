from django.db import models
import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 200)
    short_description = models.CharField(max_length = 256)
    description = models.TextField(max_length = 200)
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length = 100)
    description = models.TextField(max_length = 200)
    course = models.ForeignKey('Course')
    order =  models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    skype = models.CharField(max_length = 100)
    courses = models.ManyToManyField('Course')