from django.db import models
from coaches.models import Coach
import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=256)
    description = models.TextField(max_length=200)
    coach = models.ForeignKey('coaches.Coach', related_name='coach_courses', null=True)
    assistant = models.ForeignKey('coaches.Coach', related_name='assistant_courses', null=True)
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    course = models.ForeignKey('Course')
    order =  models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject

