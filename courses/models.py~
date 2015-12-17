from django.db import models
from coaches.models import Coach
# Create your models here.\


class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.subject
