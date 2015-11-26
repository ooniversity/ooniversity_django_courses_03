from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=80)
	surname = models.CharField(max_length=80)
	date_of_birth = models.DateField('Date of Birth')
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	skype = models.CharField(max_length=40)
	courses = models.ManyToManyField('courses.Course')

	def __unicode__(self):
		return self.name + ' ' + self.surname
