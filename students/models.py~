from django.db import models
# Create your models here.
from courses.models import Course
#import courses.models


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='12-34-56')
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    #s = ' '
    #seq = (name, surname)
    #full_name = s.join(seq)

    #def __unicode__(self):              # __unicode__ on Python 2
        #return self.full_name

    def get_full_name(self):
        #"Returns the person's full name."
        return '%s %s' % (self.name, self.surname)
    full_name = property(get_full_name)

    #def get_courses(self):
        #return self.courses.all().order_by('id').values_list('name')
        #if self.courses:
            #return '%s' % " / ".join([courses.name for courses in self.courses.all()])
            #return courses