# -*- coding:UTF-8 -*-
from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=100)                     # название
    short_description = models.CharField(max_length=300)        # краткое описание
    description = models.TextField()                            # полное описание
    coach = models.ForeignKey (Coach, blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey (Coach, blank=True, null=True, related_name='assistant_courses')
    
    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)                  # тема
    description = models.TextField()                            # описание
    course = models.ForeignKey('Course')                        # курс
    order = models.PositiveIntegerField()                       # номер по порядку 

    def __unicode__(self):
        return self.subject


