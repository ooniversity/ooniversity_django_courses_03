from django.db import models
#from coaches.models import Coach
from coaches.models import Coach

class Course(models.Model):
    name=models.CharField(max_length=255)
    short_description=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    coach=models.ForeignKey(Coach, related_name='course_coach', blank=True, null=True)
    assistant=models.ForeignKey(Coach, related_name='course_assistant', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject

