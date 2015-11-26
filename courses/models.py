from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=100)
	short_description = models.CharField(max_length=150)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length=100)
	description = models.TextField()
	order = models.PositiveIntegerField()
	course = models.ForeignKey(Course)

	def __unicode__(self):
		return self.subject

