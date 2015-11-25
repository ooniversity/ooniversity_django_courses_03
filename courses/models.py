from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description  = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

    def get_url(self):
        return "/courses/%i/" % self.id

class Lesson(models.Model):

    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.subject
