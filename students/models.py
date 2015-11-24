from django.db import models
from django.contrib import admin
from courses.models import Course, Lesson

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	skype = models.CharField(max_length=50)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.name
