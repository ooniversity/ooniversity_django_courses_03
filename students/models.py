import datetime
from django.db import models
from courses.models import Course


class Student(models.Model):
	name = models.CharField(max_length = 255)
	surname = models.CharField(max_length = 255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	skype = models.CharField(max_length = 255)
	courses = models.ManyToManyField('courses.Course')

	def full_name(self):
		return '%s %s' % (self.name, self.surname)

	def __unicode__(self): 
		full_name = "%s %s" % (self.name, self.surname)
		return full_name

class CourseApplication(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	course = models.ForeignKey(Course)
	package = models.CharField(max_length=50, choices=(
		('standart', 'Standart'),
		('gold', 'Gold'),
		('vip', 'VIP')))
	subscribe = models.BooleanField()
	comment = models.TextField(blank=True)
	is_active = models.BooleanField(default=True)
