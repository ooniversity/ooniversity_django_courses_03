from django.db import models



class Course(models.Model):

    name = models.CharField(max_length=255)
    short_description  = models.CharField(max_length=2048)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Lesson(models.Model):

    subject = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(max_length=255)
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return self.subject

# Create your models here.
