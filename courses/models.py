from django.db import models
<<<<<<< HEAD
from coaches.models import Coach
# Create your models here.\


class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)

    def __unicode__(self):              
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
=======


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
<<<<<<< HEAD
    coach = models.ForeignKey('coaches.Coach', related_name='coach_courses', blank=True, null=True)
    assistant = models.ForeignKey('coaches.Coach', related_name='assistant_courses',blank=True, null=True)
=======
    #coach = models.ForeignKey('coaches.Coach', related_name='coach_courses', blank=True, null=True)
    #assistant = models.ForeignKey('coaches.Coach', related_name='assistant_courses',blank=True, null=True)
>>>>>>> fb8e773dc2544433f2f086ca476591072179281d

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=255)
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

<<<<<<< HEAD
    def __unicode__(self):              
=======
    def __unicode__(self):
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
        return self.subject
