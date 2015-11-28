from django.db import models
from django.contrib.auth.models import User
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=225)
    short_description  = models.CharField(max_length=225)
    description = models.TextField()
    coach = models.ForeignKey(User, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(User, related_name='assistant_courses', null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject   = models.CharField(max_length=225)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.subject


