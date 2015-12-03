from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    courses = models.ManyToManyField('courses.Course')

    def __unicode__(self):
        return self.name


class CourseApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    course = models.ForeignKey(Course)
    package = models.CharField(max_length=16, choices=(
        ('standart', 'standart'),
        ('gold', 'Gold'),
        ('vip', 'VIP')), default='standart')
    news_subscribe = models.BooleanField(default=True)
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
