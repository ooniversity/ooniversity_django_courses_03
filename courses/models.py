from django.db import models
from coaches.models import Coach

class Course(models.Model):
	name = models.CharField(max_length=1000)
	short_description = models.CharField(max_length=1000)
	description = models.TextField()
	coach = models.ForeignKey('coaches.Coach', null=True, related_name='coach_courses')
	assistant = models.ForeignKey('coaches.Coach', null=True, related_name='assistant_courses')

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length=1000)
	description = models.TextField()
	order = models.PositiveIntegerField()
	course = models.ForeignKey(Course)

	def __unicode__(self):
		return self.subject

