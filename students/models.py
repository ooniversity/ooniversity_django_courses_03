from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 100)
	surname = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	skype = models.CharField(max_length = 100)
	courses = models.ManyToManyField(Course)

	def __unicode__(self): 
		full_name = "%s %s" % (self.name, self.surname)
		return full_name

	#def get_absolute_url(self):
	#return reverse('students:list_view')