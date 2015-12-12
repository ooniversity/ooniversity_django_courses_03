# -*- coding:UTF-8 -*-
from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse


class Course(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
    name = models.CharField(verbose_name=u'Name of course', max_length = 255)
=======
    name = models.CharField(max_length = 100)
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2
=======
    name = models.CharField(verbose_name=u'Name of course', max_length = 255)
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
    short_description = models.CharField(max_length = 255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length = 100)
    description = models.TextField()
    course = models.ForeignKey('Course')
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject


