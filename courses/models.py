from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=225)
    short_description  = models.CharField(max_length=225)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='+')
    assistant = models.ForeignKey(Coach, related_name='+')
    
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject   = models.CharField(max_length=225)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.subject


