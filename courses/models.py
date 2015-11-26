# -*- coding: utf-8 -*-
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 255, help_text = u'название')
    short_description = models.CharField(max_length = 255, help_text = u'краткое описание', null = True, blank = True)
    description = models.TextField(help_text = u'полное описание', null = True, blank = True)
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length = 255, help_text = u'тема')
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject
