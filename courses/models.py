from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey('coaches.Coach', related_name='coach_courses', blank=True, null=True)
    assistant = models.ForeignKey('coaches.Coach', related_name='assistant_courses',blank=True, null=True)

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
