from django.db import models

# Course
class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

# Lessons
class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject

