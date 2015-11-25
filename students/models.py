from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=50)
	courses = models.ManyToManyField(Course)
	

	def full_name(self):
		return '%s %s' % (self.name, self.surname)

