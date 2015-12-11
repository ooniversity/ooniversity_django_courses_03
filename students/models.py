from django.db import models
from django.core.urlresolvers import reverse_lazy

class Student(models.Model):
	name = models.CharField(max_length=80)
	surname = models.CharField(max_length=80)
	date_of_birth = models.DateField('Date of Birth')
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	skype = models.CharField(max_length=40)
	courses = models.ManyToManyField('courses.Course',)

	def full_name(self):
		return self.name + ' ' + self.surname

	def __unicode__(self):
		return self.full_name()

	def get_absolute_url(self):
		return reverse_lazy('students:list_view')
