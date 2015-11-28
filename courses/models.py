from django.db import models


# Create your models here.
class Course(models.Model):
    class Meta():
        db_table = 'courses'

    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    # __unicode__ on Python 2
    def __unicode__(self):
        return self.name

    # __str__ on Python 3
    def __str__(self):
        return self.name

    # def get_url(self):
    #    return '/courses/%{num}/'.format(num=self.id)


class Lesson(models.Model):
    class Meta():
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