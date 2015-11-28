from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	address = models.CharField(max_length=200)
	skype = models.CharField(max_length=200)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.name +" " + self.surname
