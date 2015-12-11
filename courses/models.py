# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from coaches.models import Coach

class Course (models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def  __unicode__(self):
        return self.name

class Lesson (models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def  __unicode__(self):
        return self.subject
