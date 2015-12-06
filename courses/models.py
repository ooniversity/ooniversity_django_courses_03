from django.db import models
from coaches.models import Coach


# Create your models here.
class Course(models.Model):
    # class Meta():
    #    db_table = 'courses'

    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    coach = models.ForeignKey(Coach, related_name='coach_courses', blank=True, null=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', blank=True, null=True)

    # __unicode__ on Python 2
    def __unicode__(self):
        return self.name

    # __str__ on Python 3
    def __str__(self):
        return self.name

    # def get_url(self):
    #    return '/courses/%{num}/'.format(num=self.id)


class Lesson(models.Model):
    class Meta:
        db_table = 'lesson'

    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    # __unicode__ on Python 2
    def __unicode__(self):
        return self.subject

    # __str__ on Python 3
    def __str__(self):
        return self.subject
