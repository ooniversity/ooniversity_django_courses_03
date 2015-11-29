from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=70)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='courses_coach')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='courses_assistant')

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description= models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField(unique=False)

    def __unicode__(self):
        return self.subject

